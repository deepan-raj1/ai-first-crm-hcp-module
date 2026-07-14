import { useState } from "react";
import axios from "axios";

function AIChat() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!message.trim()) return;

    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/api/ai/chat",
        {
          message,
        }
      );

      setResponse(res.data);
    } catch (error) {
      console.error(error);
      alert("Something went wrong.");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>AI CRM Assistant</h1>

      <textarea
        rows={6}
        cols={70}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Describe your interaction..."
      />

      <br />
      <br />

      <button onClick={sendMessage}>
        {loading ? "Processing..." : "Send"}
      </button>

      <br />
      <br />

      <pre>
        {JSON.stringify(response, null, 2)}
      </pre>
    </div>
  );
}

export default AIChat;