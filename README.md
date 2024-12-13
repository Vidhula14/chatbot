# Chatbot Using Streamlit and Groq API

This project is a simple chatbot built using **Streamlit** for the user interface and the **Groq API** for generating AI responses. The chatbot takes user inputs, sends them to the Groq API, and displays the generated responses.

## Features
- User-friendly interface built with Streamlit.
- AI-powered responses using the Groq API.
- Supports conversational-style interaction.
- Handles errors gracefully with informative messages.

## Prerequisites

Before running the application, ensure you have the following:
- Python 3.7 or higher
- An API key for the Groq service

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Groq API key:
   - Create a `.env` file in the project root directory.
   - Add your API key in the following format:
     ```env
     GROQ_API_KEY=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
     ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open the local URL provided by Streamlit (usually `http://localhost:8501`) in your web browser.

3. Type your queries in the input box, and the chatbot will respond.

## File Structure

```
├── main.py            # Main application code
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── .env               # API key (excluded from version control)
```

## Dependencies

- Streamlit
- Groq API SDK (install via pip)

## Error Handling
- If there is an issue generating a response, the chatbot displays an error message with details about the problem.

## Future Improvements
- Add support for more AI models.
- Enhance the user interface with additional customization options.
- Integrate session management for better conversational context.

## Contributing

Contributions are welcome! Please fork this repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Disclaimer
Ensure you keep your API key confidential. Do not expose sensitive credentials in your code or repository. Use `.gitignore` to exclude files like `.env` containing sensitive information.
