const API_URL = "https://hr6vzc0lxb.execute-api.us-east-1.amazonaws.com/prod/chat";

async function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const userMessage = input.value.trim();
  
  if (!userMessage) return;

  // Show user message
  const userDiv = document.createElement("div");
  userDiv.className = "message user";
  userDiv.textContent = "You: " + userMessage;
  chatBox.appendChild(userDiv);

  input.value = "";

  // Send request to API Gateway
  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();

    // Show bot reply
    const botDiv = document.createElement("div");
    botDiv.className = "message bot";
    botDiv.textContent = "Bot: " + (data.reply || "Error: No reply");
    chatBox.appendChild(botDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (error) {
    console.error(error);
    const botDiv = document.createElement("div");
    botDiv.className = "message bot";
    botDiv.textContent = "Bot: Error connecting to API";
    chatBox.appendChild(botDiv);
  }
}
