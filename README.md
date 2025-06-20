
# 🧠 Memory-Powered Chatbot using Hugging Face Transformers

This is a simple Python-based chatbot that maintains recent conversation context using a sliding window memory buffer and generates human-like responses using Hugging Face-hosted models such as `LLaMA 2 Chat` or `Hermes`.

---

## 🚀 Features

- 💬 Conversational chatbot with short-term memory
- 🧠 Sliding window memory for recent exchanges
- 🤖 Hugging Face Inference API integration
- 🧹 Response cleaning for smoother interaction
- ✅ Simple terminal interface

---

## 📁 Project Structure

```

📦 chatbot/
├── interface.py        # Main entry point to run the chatbot
├── model_loader.py     # Loads model from Hugging Face Inference API
├── chat_memory.py      # Maintains conversation history (sliding window)
└── README.md           # Project documentation

````

---

## 📦 Requirements

Install dependencies with:

```bash
pip install huggingface_hub
````

You also need a **Hugging Face API Token**. Create one at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## 🔐 Setup Environment

Before running the chatbot, set your HF token:

* **Windows:**

```bash
set HF_TOKEN=your_api_token_here
```

* **Linux/macOS:**

```bash
export HF_TOKEN=your_api_token_here
```

---

## 🧪 Running the Chatbot

```bash
python interface.py
```

You'll see:

```
Chatbot ready! Type '/exit' to quit.
You: my name is Sid
Bot: Nice to meet you, Sid!
You: what's my name?
Bot: Your name is Sid.
```

---

## 🧠 How Memory Works

This chatbot uses a **sliding window** buffer (default: last 3 turns) to simulate short-term memory.
It maintains context like this:

```
User: my name is Sid
Assistant: Nice to meet you, Sid!
User: what's my name?
Assistant: Your name is Sid.
```

This makes it feel like you're talking to a real assistant!

---

## 🛠️ Design Decisions

* Manual prompt formatting: `User: ... \n Assistant: ...` to simulate conversation history.
* Hugging Face `InferenceClient.text_generation()` is used instead of chat APIs for flexibility.
* Tested models:

  * ✅ `meta-llama/Llama-2-7b-chat-hf`
  * ✅ `NousResearch/Hermes-2-Pro-Mistral-7B`

---
## 🤝 Contributing

Feel free to fork, clone, and contribute!
Pull requests and issues are welcome.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

* [Hugging Face Inference API](https://huggingface.co/inference-api)
* LLaMA 2 by Meta AI
* Mistral & Hermes by Nous Research

---

## 🧑‍💻 Made by

**Siddhant Gondane**
*Student, AI & Machine Learning | Chatbot + NLP Enthusiast*

