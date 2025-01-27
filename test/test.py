#........................................one to one conversation
# import google.generativeai as genai

# # Configure your Google API Key
# genai.configure(api_key="AIzaSyBcX-tIfvxHUEvbMn3QMIWWvP1fKs5fVDw")

# # Function to handle user input and generate a response
# def main():
#     print("Welcome to the AI Text Generator!")
#     while True:
#         user_input = input("\nEnter your prompt (or type 'exit' to quit): ")
#         if user_input.lower() == 'exit':
#             print("Goodbye!")
#             break
        
#         # Call the Google Generative AI API
#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(user_input)
        
#         # Print the generated response
#         print(f"\nAI Response:\n{response.text}")

# if __name__ == "__main__":
#     main()





import google.generativeai as genai

# Configure your Google API Key
genai.configure(api_key="AIzaSyBcX-tIfvxHUEvbMn3QMIWWvP1fKs5fVDw")

# Start a chat session
def main():
    print("Welcome to the AI Chat!")
    print("Type your message to the AI or type 'exit' to quit.")

    # Initialize the chat history
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )

    while True:
        # User input
        user_message = input("\nYou: ")
        if user_message.lower() == 'exit':
            print("Goodbye!")
            break

        # Send message to the chat
        response = chat.send_message(user_message)

        # Print the response from the AI
        print(f"AI: {response.text}")

if __name__ == "__main__":
    main()

