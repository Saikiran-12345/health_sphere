from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.core.rbac import RoleChecker
from app.models.user import UserRole
from typing import List, Dict

allow_doctors_only = RoleChecker([UserRole.DOCTOR, UserRole.ADMIN])

router = APIRouter(prefix="/api/telemedicine", tags=["Telemedicine"], dependencies=[Depends(allow_doctors_only)])

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, room_id: str, websocket: WebSocket):
        await websocket.accept()
        if room_id not in self.active_connections:
            self.active_connections[room_id] = []
        self.active_connections[room_id].append(websocket)

    def disconnect(self, room_id: str, websocket: WebSocket):
        if room_id in self.active_connections:
            self.active_connections[room_id].remove(websocket)
            if not self.active_connections[room_id]:
                del self.active_connections[room_id]

    async def broadcast(self, room_id: str, message: str):
        if room_id in self.active_connections:
            for connection in self.active_connections[room_id]:
                await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await manager.connect(room_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(room_id, f"Message: {data}")
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
        await manager.broadcast(room_id, "User disconnected.")
