from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
from django.conf import settings

# Configure the Google API Key
genai.configure(api_key=settings.GEMINI_API_KEY)

# Initialize the chat model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)


def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        if not user_message:
            return JsonResponse({"error": "No message provided"}, status=400)

        # Send the user's message to the chat model
        response = chat.send_message(user_message)
        return JsonResponse({"response": response.text})
    
    return render(request, "chatapp/chat.html")

