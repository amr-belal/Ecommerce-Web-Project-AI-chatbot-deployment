
import { MessageCircle } from "lucide-react"; // أيقونة محادثة
import "../style/ChatWidget.css"; 
import React, { useState } from "react";



const ChatWidget = () => {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [extraData, setExtraData] = useState(null);

  const sendMessage = async () => {
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { sender: "user", text: input }]);

    try {
      const res = await fetch("http://localhost:8000/user_response", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: "Amr",
          message: input,
        }),
      });

      const data = await res.json();

      setMessages((prev) => [...prev, { sender: "bot", text: data.reply }]);

      setExtraData({
        location: data.location,
        weather: data.weather,
        keywords: data.keywords,
      });

    } catch (err) {
      console.error("Error connecting to API:", err);
    }

    setInput("");
  };

  return (
    <div className="chat-widget">
      {!open ? (
        <button className="chat-btn" onClick={() => setOpen(true)}>
          <MessageCircle size={28} />
        </button>
      ) : (
        <div className="chat-box">
          <div className="chat-header">
            <span>Aria 🥰</span>
            <button onClick={() => setOpen(false)}>×</button>
          </div>

          {/* --- Dashboard فوق الشات --- */}
          {extraData && (
            <div className="chat-dashboard">
              <p><b>📍 {extraData.location?.[4]}</b></p>
              <p>🌤️ {extraData.weather?.[0]} ({extraData.weather?.[1]}°C)</p>
              <div className="keywords">
                {extraData.keywords.map((kw, i) => (
                  <span key={i} className="tag">{kw}</span>
                ))}
              </div>
            </div>
          )}

          {/* --- الرسائل --- */}
          <div className="chat-messages">
            {messages.map((msg, i) => (
              <div key={i} className={`msg ${msg.sender}`}>
                {msg.text}
              </div>
            ))}
          </div>

          
          <div className="chat-input">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Type a message..."
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatWidget;
