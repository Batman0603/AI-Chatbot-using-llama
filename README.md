# 🤖 Friendly Chatbot

![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-blue)
![Bolt AI](https://img.shields.io/badge/Frontend-Bolt%20AI-yellow)
![LLM](https://img.shields.io/badge/Powered%20By-LLaMA%20%7C%20Together%20AI-brightgreen)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-blueviolet)

> A simple, intuitive, and fun-to-use AI chatbot built using Bolt AI (Frontend), Flask (Backend), and LLaMA model (API via Together AI). Ideal for anyone looking to understand full-stack LLM chatbot integration!

---

## 🌟 Demo Preview

![Chatbot Demo](https://media.giphy.com/media/v1.YOUR_CHATBOT_GIF_LINK_HERE/giphy.gif)

---

## 🧠 What is this project?

This is a **friendly chatbot** interface that uses:

- **Frontend**: Designed with prompts using **Bolt AI**
- **Backend**: Flask Python server that handles incoming messages
- **LLM Model**: **LLaMA model** via **Together AI API** for generating intelligent responses

It acts like a virtual assistant that replies to your messages based on advanced natural language understanding.

---

## ✨ Features

- ✅ AI-Powered Conversations (via LLaMA from Together AI)  
- 🌐 Clean & responsive frontend (Bolt AI generated)  
- 🧠 Flask backend to handle API calls  
- 🚀 Real-time message flow between user and LLM  
- 🔐 Secure API interaction  

---

## 📦 Tech Stack

| Tech       | Usage                                  |
|------------|----------------------------------------|
| 🐍 Python  | Flask backend                          |
| 📡 API     | Together AI (LLaMA model)              |
| 🧠 AI/LLM   | LLaMA from Together AI                 |
| 🧪 Frontend| Bolt AI (Prompt-Generated UI)          |
| 📄 JSON    | Message passing structure              |

---

## 🏗️ How to Build the Project

> Follow these steps to create your own chatbot from scratch:

### 🔹 1. **Design Your Frontend using Bolt AI**
- Go to [https://boltai.app](https://boltai.app)  
- Prompt: _"Create a chat UI for friendly chatbot"_  
- Export the generated HTML/CSS/JS or integrate directly  

### 🔹 2. **Set Up Flask Backend**
```bash
mkdir friendly-chatbot
cd friendly-chatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install flask requests

🔹 3. Get API Key from Together AI
Visit: https://together.ai

Sign up and copy your API key

Save it in a .env file:

TOGETHER_API_KEY=your_api_key_here

🔹 4. Connect Frontend ↔ Backend
Use fetch() or axios to send user input to your Flask backend

Flask handles the message, calls Together AI API, and returns response

## 📁 Folder Structure

friendly-chatbot/
│
├── backend/
│ ├── app.py # Flask server
│ ├── .env # API key file
│ └── requirements.txt # Python dependencies
│
├── project/ # Bolt AI frontend
│ └── [prompt-based UI files]
│
└── README.md

🧪 Running the Project
🔹 1. Clone the Repo

git clone https://github.com/your-username/friendly-chatbot.git
cd friendly-chatbot

🔹 2. Install Backend Requirements

pip install -r requirements.txt

🔹 3. Create .env File

touch .env
# Add your API key
TOGETHER_API_KEY=your_key

🔹 4. Run the Backend

python app.py

🔹 5. Open the Frontend

Open index.html from the frontend folder in your browser
Or host it using Netlify/Vercel/etc.

💬 Sample API Flow

POST /chat
{
  "message": "Hi there!"
}
Response:
{
  "response": "Hello! How can I assist you today?"
}

💡 Future Improvements

Add user authentication for personalized chat experience

Store chat history in a database

Deploy on platforms like Vercel (Frontend) + Render/Railway (Backend)

📬 Feedback
If you loved it or faced any issues, feel free to raise an issue or DM me!

📢 Final Words
Building this chatbot taught me how frontend, backend, and AI models can work together beautifully.
Enjoy chatting with your virtual friend!

