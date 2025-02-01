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

    let chatBox = document.createElement("div");
    chatBox.id = "chat-box";
    chatBox.style.position = "fixed";
    chatBox.style.bottom = "80px";
    chatBox.style.right = "20px";
    chatBox.style.width = "300px";
    chatBox.style.height = "400px";
    chatBox.style.background = "#fff";
    chatBox.style.border = "1px solid #ccc";
    chatBox.style.display = "none";
    chatBox.style.padding = "10px";
    chatBox.style.overflowY = "scroll";
    document.body.appendChild(chatBox);

    let chatInput = document.createElement("input");
    chatInput.type = "text";
    chatInput.placeholder = "Ask something...";
    chatInput.style.width = "100%";
    chatBox.appendChild(chatInput);

    let sendButton = document.createElement("button");
    sendButton.innerText = "Send";
    sendButton.style.width = "100%";
    sendButton.onclick = function () {
        let userQuestion = chatInput.value;
        chatBox.innerHTML += `<p><strong>You:</strong> ${userQuestion}</p>`;
        chatInput.value = "";

        fetch("/chatbot/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: userQuestion })
        })
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<p><strong>Chatbot:</strong> ${data.answer}</p>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    };

    chatBox.appendChild(sendButton);

    chatIcon.onclick = function () {
        chatBox.style.display = (chatBox.style.display === "none") ? "block" : "none";
    };
});
