# ✨ Gemini Chat Assistant

A professional, feature-rich chatbot application built with Streamlit and Google's Gemini AI.

## 🌟 Features

- **Real-time Streaming**: Watch responses appear word-by-word
- **Multiple Models**: Choose between Gemini 1.5 Pro, Flash, or 1.0 Pro
- **Customizable Parameters**: Adjust temperature, max tokens, and top-p
- **System Instructions**: Set custom behavior and personality
- **Conversation Management**: Clear and export chat history
- **Professional UI**: Clean, modern interface with custom styling
- **Error Handling**: Robust error management and user feedback
- **Secure**: API keys handled securely through environment

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Your API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 3. Run the Application

```bash
streamlit run gemini_chatbot.py
```

### 4. Configure

1. Enter your API key in the sidebar
2. Choose your preferred model
3. Adjust parameters as needed
4. Start chatting!

## 🎮 Usage Guide

### Model Selection

- **Gemini 1.5 Flash**: Fast responses, good for general chat (recommended)
- **Gemini 1.5 Pro**: More capable, better for complex tasks
- **Gemini 1.0 Pro**: Stable, reliable option

### Parameters

- **Temperature** (0.0-2.0): Controls randomness
  - Lower (0.0-0.3): More focused, deterministic
  - Medium (0.7-1.0): Balanced creativity
  - Higher (1.5-2.0): More creative, diverse

- **Max Tokens**: Maximum response length
  - 256-1024: Short responses
  - 2048: Standard responses (recommended)
  - 4096-8192: Long-form content

- **Top P** (0.0-1.0): Nucleus sampling
  - 0.95 recommended for most use cases

### System Instructions

Customize the AI's behavior by modifying system instructions:

```
You are a helpful coding assistant specializing in Python.
Always provide code examples and explain your solutions.
```

### Conversation Management

- **Clear Chat**: Remove all messages and start fresh
- **Export Chat**: Download conversation as text file
- **Message Counter**: Track conversation length

## 💡 Example Use Cases

### 1. Coding Assistant
```
System Instruction: "You are an expert Python developer. Provide clean, 
well-documented code with explanations."

Prompt: "Create a class for a binary search tree"
```

### 2. Writing Helper
```
System Instruction: "You are a professional editor. Help improve writing 
clarity, grammar, and style."

Prompt: "Review this paragraph: [your text]"
```

### 3. Learning Tutor
```
System Instruction: "You are a patient teacher. Explain concepts clearly 
with examples and check understanding."

Prompt: "Explain how neural networks work"
```

### 4. Brainstorming Partner
```
System Instruction: "You are a creative brainstorming partner. Generate 
diverse, innovative ideas."

Prompt: "Ideas for a sustainable urban garden project"
```

## 🔧 Advanced Configuration

### Environment Variables

For production, set your API key as an environment variable:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Then modify the code to read from environment:

```python
import os
api_key = os.getenv("GOOGLE_API_KEY", "")
```

### Custom Styling

Edit the CSS in the `st.markdown()` section to customize colors, fonts, and layout.

### Add Features

The code is modular and easy to extend:

- Add file upload support
- Integrate with external APIs
- Add conversation persistence (SQLite, MongoDB)
- Implement user authentication
- Add multi-language support

## 📊 Model Comparison

| Feature | Gemini 1.5 Flash | Gemini 1.5 Pro | Gemini 1.0 Pro |
|---------|------------------|----------------|----------------|
| Speed | ⚡⚡⚡ Fast | ⚡⚡ Medium | ⚡⚡ Medium |
| Capability | ⭐⭐⭐ Good | ⭐⭐⭐⭐ Excellent | ⭐⭐ Good |
| Context | 1M tokens | 1M tokens | 32K tokens |
| Best For | Chat, Q&A | Complex tasks | General use |

## 🛡️ Best Practices

1. **API Key Security**: Never commit API keys to version control
2. **Rate Limiting**: Be mindful of API usage limits
3. **Error Handling**: The app handles errors gracefully
4. **Temperature**: Start with 0.7 and adjust based on needs
5. **System Instructions**: Be specific for best results

## 🐛 Troubleshooting

### "Invalid API Key"
- Verify your API key is correct
- Check if the key has necessary permissions
- Ensure the Gemini API is enabled in your Google Cloud project

### Slow Responses
- Try switching to Gemini 1.5 Flash
- Reduce max_tokens setting
- Check your internet connection

### Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Update packages: `pip install --upgrade streamlit google-generativeai`

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 🔗 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Google AI Studio](https://makersuite.google.com/)

## ⚡ Performance Tips

1. Use Flash model for everyday chat
2. Keep system instructions concise
3. Clear chat history periodically
4. Use appropriate max_tokens for your use case
5. Adjust temperature based on task type

## 🎯 Future Enhancements

- [ ] Image upload and analysis
- [ ] Voice input/output
- [ ] Conversation branching
- [ ] Multi-turn context management
- [ ] User profiles and preferences
- [ ] Response regeneration
- [ ] Code syntax highlighting
- [ ] Markdown rendering
- [ ] Search within conversations

---

Built with ❤️ using Streamlit and Google Gemini AI
