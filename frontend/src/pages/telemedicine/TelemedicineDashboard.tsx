import React, { useState, useEffect } from 'react';
import { Video, Mic, MicOff, VideoOff, PhoneOff, MessageSquare } from 'lucide-react';

export const TelemedicineDashboard: React.FC = () => {
  const [inCall, setInCall] = useState(false);
  const [micOn, setMicOn] = useState(true);
  const [videoOn, setVideoOn] = useState(true);
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState("");

  const handleStartCall = () => setInCall(true);
  const handleEndCall = () => setInCall(false);

  return (
    <div className="bg-white rounded-lg shadow h-full flex flex-col p-6">
      <div className="flex justify-between items-center mb-6 border-b pb-4">
        <h2 className="text-2xl font-bold text-gray-800 flex items-center gap-2">
          <Video className="text-blue-600"/> Telemedicine & Virtual Consultations
        </h2>
        {!inCall && (
          <button onClick={handleStartCall} className="bg-blue-600 text-white px-4 py-2 rounded shadow hover:bg-blue-700">
            Start Consultation Room
          </button>
        )}
      </div>

      {!inCall ? (
        <div className="flex-1 flex flex-col items-center justify-center text-gray-500">
          <Video size={64} className="text-gray-300 mb-4" />
          <h3 className="text-xl font-medium">No Active Consultations</h3>
          <p>Click "Start Consultation Room" to generate a secure video link.</p>
        </div>
      ) : (
        <div className="flex-1 flex gap-6">
          {/* Video Area */}
          <div className="flex-1 flex flex-col bg-gray-900 rounded-lg overflow-hidden relative">
            <div className="flex-1 flex items-center justify-center text-white">
              {videoOn ? <span className="text-2xl">Camera Active (Mock)</span> : <VideoOff size={64} className="text-gray-600"/>}
            </div>
            
            {/* Controls */}
            <div className="bg-gray-800 p-4 flex justify-center gap-4">
              <button onClick={() => setMicOn(!micOn)} className={`p-4 rounded-full ${micOn ? 'bg-gray-700 text-white hover:bg-gray-600' : 'bg-red-500 text-white'}`}>
                {micOn ? <Mic size={24}/> : <MicOff size={24}/>}
              </button>
              <button onClick={() => setVideoOn(!videoOn)} className={`p-4 rounded-full ${videoOn ? 'bg-gray-700 text-white hover:bg-gray-600' : 'bg-red-500 text-white'}`}>
                {videoOn ? <Video size={24}/> : <VideoOff size={24}/>}
              </button>
              <button onClick={handleEndCall} className="p-4 rounded-full bg-red-600 text-white hover:bg-red-700">
                <PhoneOff size={24}/>
              </button>
            </div>
          </div>
          
          {/* Chat Area */}
          <div className="w-80 flex flex-col border rounded-lg bg-gray-50">
            <div className="p-4 border-b bg-white flex items-center gap-2 font-bold text-gray-700">
              <MessageSquare size={18}/> Consultation Chat
            </div>
            <div className="flex-1 p-4 overflow-auto space-y-4">
              {messages.map((m, i) => (
                <div key={i} className="bg-blue-100 text-blue-900 p-2 rounded-lg text-sm max-w-[85%] self-end">
                  {m}
                </div>
              ))}
            </div>
            <div className="p-3 bg-white border-t flex gap-2">
              <input 
                value={input} 
                onChange={e => setInput(e.target.value)}
                onKeyDown={e => { if (e.key === 'Enter') { setMessages([...messages, input]); setInput(''); } }}
                className="flex-1 border rounded px-2 py-1 text-sm" 
                placeholder="Type a message..." 
              />
              <button onClick={() => { setMessages([...messages, input]); setInput(''); }} className="bg-blue-600 text-white px-3 rounded text-sm">Send</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
