document.addEventListener("DOMContentLoaded", function () {
    let chatIcon = document.createElement("div");
    chatIcon.innerHTML = "💬";
    chatIcon.id = "chat-icon";
    chatIcon.style.position = "fixed";
    chatIcon.style.bottom = "20px";
    chatIcon.style.right = "20px";
    chatIcon.style.background = "#007bff";
    chatIcon.style.color = "#fff";
    chatIcon.style.padding = "15px";
    chatIcon.style.borderRadius = "50%";
    chatIcon.style.cursor = "pointer";
    chatIcon.style.fontSize = "24px";
    document.body.appendChild(chatIcon);

    let chatContainer = document.createElement("div");
    chatContainer.id = "chat-container";
    chatContainer.style.position = "fixed";
    chatContainer.style.bottom = "80px";
    chatContainer.style.right = "20px";
    chatContainer.style.width = "320px";
    chatContainer.style.height = "450px";
    chatContainer.style.background = "#fff";
    chatContainer.style.border = "1px solid #ccc";
    chatContainer.style.display = "none";
    chatContainer.style.borderRadius = "10px";
    chatContainer.style.overflow = "hidden";
    chatContainer.style.boxShadow = "0px 4px 10px rgba(0,0,0,0.1)";
    document.body.appendChild(chatContainer);

    let chatHeader = document.createElement("div");
    chatHeader.innerText = "StudentBot Chat";
    chatHeader.style.background = "#007bff";
    chatHeader.style.color = "#fff";
    chatHeader.style.padding = "10px";
    chatHeader.style.textAlign = "center";
    chatContainer.appendChild(chatHeader);

    let chatBox = document.createElement("div");
    chatBox.id = "chat-box";
    chatBox.style.height = "360px";
    chatBox.style.padding = "10px";
    chatBox.style.overflowY = "auto";
    chatBox.style.display = "flex";
    chatBox.style.flexDirection = "column";
    chatContainer.appendChild(chatBox);

    let inputContainer = document.createElement("div");
    inputContainer.style.display = "flex";
    inputContainer.style.borderTop = "1px solid #ccc";
    inputContainer.style.padding = "5px";

    let chatInput = document.createElement("input");
    chatInput.type = "text";
    chatInput.id = "chat-input";
    chatInput.placeholder = "Type a message...";
    chatInput.style.flex = "1";
    chatInput.style.padding = "8px";
    chatInput.style.border = "none";
    chatInput.style.outline = "none";

    let sendButton = document.createElement("button");
    sendButton.innerText = "Send";
    sendButton.style.background = "#007bff";
    sendButton.style.color = "#fff";
    sendButton.style.border = "none";
    sendButton.style.padding = "8px 15px";
    sendButton.style.cursor = "pointer";

    function sendMessage() {
        let userQuestion = chatInput.value.trim();
        if (!userQuestion) return;

        let currentPageURL = window.location.href;

        let userMessage = document.createElement("div");
        userMessage.innerHTML = `<strong>You:</strong> ${userQuestion}`;
        userMessage.style.background = "#f1f1f1";
        userMessage.style.padding = "8px";
        userMessage.style.borderRadius = "5px";
        userMessage.style.margin = "5px 0";
        userMessage.style.alignSelf = "flex-end";
        chatBox.appendChild(userMessage);

        chatInput.value = "";

        fetch("/chatbot/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: userQuestion, current_url: currentPageURL })
        })
        .then(response => response.json())
        .then(data => {
            let botMessage = document.createElement("div");
            botMessage.innerHTML = `<strong>Chatbot:</strong> ${data.answer}`;
            botMessage.style.background = "#007bff";
            botMessage.style.color = "#fff";
            botMessage.style.padding = "8px";
            botMessage.style.borderRadius = "5px";
            botMessage.style.margin = "5px 0";
            botMessage.style.alignSelf = "flex-start";
            chatBox.appendChild(botMessage);
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    }

    sendButton.onclick = sendMessage;

    chatInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });

    inputContainer.appendChild(chatInput);
    inputContainer.appendChild(sendButton);
    chatContainer.appendChild(inputContainer);

    chatIcon.onclick = function () {
        chatContainer.style.display = (chatContainer.style.display === "none") ? "block" : "none";
    };
});
