import asyncio
from datetime import datetime

async def background_daily_report_generator():
    """
    Simulated background task runner for massive data crunching at midnight.
    """
    print(f"[{datetime.utcnow()}] Starting massive background report generation...")
    await asyncio.sleep(5) # Simulate heavy IO
    print(f"[{datetime.utcnow()}] Background reports generated and cached successfully.")

async def background_inventory_reorder_check():
    """
    Simulated worker that checks pharmacy inventory against reorder levels.
    """
    print(f"[{datetime.utcnow()}] Scanning inventory for shortages...")
    await asyncio.sleep(2)
    print(f"[{datetime.utcnow()}] Inventory scan complete. Auto-purchase orders dispatched.")
