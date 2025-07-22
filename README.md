# 🤖✨ Friendly AI Chatbot

<div align="center">

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&height=70&lines=Welcome+to+Friendly+Chatbot!;AI+Powered+Conversations;Built+with+Flask+%26+LLaMA)

![Made with Flask](https://img.shields.io/badge/Made%20with-Flask-1f425f?style=for-the-badge&logo=flask&logoColor=white)
![Bolt AI](https://img.shields.io/badge/Frontend-Bolt%20AI-FFD43B?style=for-the-badge&logo=lightning&logoColor=black)
![LLM](https://img.shields.io/badge/Powered%20By-LLaMA-00D4AA?style=for-the-badge&logo=meta&logoColor=white)
![Open Source](https://img.shields.io/badge/Open%20Source-💜-blueviolet?style=for-the-badge)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

---

## 🎯 **Project Overview**

> **A modern, intelligent chatbot that brings AI conversations to life!** 
> 
> This project demonstrates the perfect harmony between frontend design, backend architecture, and cutting-edge AI technology.

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="100">
</div>

### 🧠 **What Makes This Special?**

Our chatbot leverages:
- 🎨 **Frontend**: Beautiful, responsive UI crafted with **Bolt AI**
- ⚙️ **Backend**: Robust Flask server handling seamless API communication  
- 🚀 **AI Engine**: Powerful **LLaMA model** via **Together AI** for intelligent responses
- 💬 **Experience**: Natural, context-aware conversations that feel human-like

---

## ✨ **Key Features**

<table>
<tr>
<td>

🤖 **AI-Powered Conversations**
> Smart responses powered by LLaMA

🌐 **Responsive Design** 
> Beautiful UI that works on all devices

⚡ **Real-time Communication**
> Instant message flow between user and AI

</td>
<td>

🔒 **Secure API Integration**
> Protected endpoints and safe data handling

🎨 **Modern Interface**
> Clean, intuitive chat experience

🔧 **Easy to Extend**
> Modular architecture for future enhancements

</td>
</tr>
</table>

---

## 🛠️ **Tech Stack**

<div align="center">

| Technology | Purpose | Icon |
|------------|---------|------|
| **Python + Flask** | Backend API Server | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" width="40"> |
| **Together AI** | LLaMA Model API | 🧠 |
| **Bolt AI** | Frontend Generation | ⚡ |
| **HTML/CSS/JS** | User Interface | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" width="40"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" width="40"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" width="40"> |

</div>

---

## 🚀 **Quick Start Guide**

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">
</div>

### 📋 **Prerequisites**
- Python 3.8+
- Git
- Together AI API key

### ⚡ **Installation**

**1. Clone the Repository**
```bash
git clone https://github.com/your-username/friendly-chatbot.git
cd friendly-chatbot
```

**2. Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure Environment**
```bash
# Create .env file
touch .env

# Add your API key
echo "TOGETHER_API_KEY=your_api_key_here" > .env
```

**5. Launch the Application**
```bash
# Start backend server
python app.py

# Open frontend in browser
# Navigate to frontend folder and open index.html
```

---

## 🏗️ **Project Architecture**

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4eeccf656e44.gif" width="200">
</div>

```
friendly-chatbot/
│
├── 📁 backend/
│   ├── 🐍 app.py              # Flask server
│   ├── 🔐 .env                # API keys
│   ├── 📋 requirements.txt    # Dependencies
│   └── 🧪 utils.py           # Helper functions
│
├── 📁 frontend/
│   ├── 🎨 index.html         # Main interface
│   ├── 💄 style.css          # Styling
│   ├── ⚡ script.js          # Frontend logic
│   └── 🖼️ assets/           # Images & icons
│
├── 📁 docs/
│   └── 📚 API.md             # API documentation
│
└── 📖 README.md
```

---

## 🔌 **API Reference**

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284175-f47e74e6-592f-4c4e-b8ea-1d73b4c6ce8c.gif" width="150">
</div>

### **Chat Endpoint**

**POST** `/chat`

**Request Body:**
```json
{
  "message": "Hello, how are you?"
}
```

**Response:**
```json
{
  "response": "Hello! I'm doing great, thank you for asking. How can I help you today?",
  "timestamp": "2024-01-15T10:30:00Z",
  "status": "success"
}
```

---

## 🎨 **Building Your Frontend with Bolt AI**

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="300">
</div>

**Step-by-step Guide:**

1. **Visit** [Bolt AI](https://bolt.new)
2. **Prompt**: *"Create a modern chat interface for an AI chatbot with dark theme, message bubbles, and typing indicators"*
3. **Customize** the generated UI to match your brand
4. **Export** and integrate with your Flask backend

---

## 🌟 **Demo & Screenshots**

<div align="center">

### 💬 **Chat Interface**
*Beautiful, responsive design that adapts to any device*

<img src="https://user-images.githubusercontent.com/74038190/212284094-e50ceea7-de32-4a67-a5c2-dda3c2209c9d.gif" width="600">

### ⚡ **Real-time Responses**
*Instant AI-powered conversations*

</div>

---

## 🔮 **Future Roadmap**

<table>
<tr>
<td width="70%" valign="top">

- [ ] 🔐 **User Authentication** - Personalized chat experiences
- [ ] 💾 **Chat History** - Database integration for message persistence  
- [ ] 🌍 **Multi-language Support** - Global accessibility
- [ ] 📱 **Mobile App** - Native iOS and Android applications
- [ ] 🎙️ **Voice Integration** - Speech-to-text and text-to-speech
- [ ] 🔍 **Advanced Search** - Search through chat history
- [ ] 🎨 **Theme Customization** - Multiple UI themes
- [ ] 📊 **Analytics Dashboard** - Usage statistics and insights

</td>
<td width="30%" align="right" valign="top">

<img src="https://user-images.githubusercontent.com/74038190/212284145-bf2c01a8-c448-4f1a-b911-996024c84606.gif" width="200">

</td>
</tr>
</table>

---

## 🤝 **Contributing**

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284119-fbfd994d-8c2a-4a58-a57e-ffa1e06f289e.gif" width="300">
</div>

We love contributions! Here's how you can help:

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch (`git checkout -b amazing-feature`)
3. 💎 **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. 📤 **Push** to the branch (`git push origin amazing-feature`)
5. 🎉 **Open** a Pull Request

---

## 📜 **License**

<div align="center">

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

<img src="https://user-images.githubusercontent.com/74038190/212284126-ae0c5389-7df8-4a15-85cf-a2688e44c97d.gif" width="150">

</div>

---

## 💌 **Support & Contact**

<div align="center">

**Enjoyed this project? Give it a ⭐!**

[![GitHub followers](https://img.shields.io/github/followers/yourusername?style=social)](https://github.com/yourusername)
[![Twitter Follow](https://img.shields.io/twitter/follow/yourusername?style=social)](https://twitter.com/yourusername)

**Have questions or feedback?**
- 📧 Email: your.email@example.com
- 💬 Twitter: [@yourusername](https://twitter.com/yourusername)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/friendly-chatbot/issues)

<img src="https://user-images.githubusercontent.com/74038190/212284071-0b9d2a65-69c9-44a7-be7b-86d9a91b0238.gif" width="400">

**Made with 💜 by [Your Name]**

*Building the future, one conversation at a time.*

</div>

---

<div align="center">

### 🎉 **Thank you for checking out Friendly Chatbot!**

<img src="https://user-images.githubusercontent.com/74038190/212284103-b99a4e57-2153-4c8a-b8f4-2bb8bb04faee.gif" width="500">

**Star ⭐ this repo if you found it helpful!**

</div>
