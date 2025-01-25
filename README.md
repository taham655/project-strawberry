# 🤖 Reasoning is all you need

A powerful AI reasoning tool that combines DeepSeek's reasoning capabilities with language models to provide well-thought-out responses to your questions.

## Features

- Uses DeepSeek's reasoning model for detailed thought process
- Choice between GPT-3.5 and Llama 3.2 1B for final responses
- Beautiful CLI interface with formatted output

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/project-strawberry.git
   cd project-strawberry
   ```

2. Create a virtual environment:

   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install openai python-dotenv
   ```

## API Key Setup

This project requires API keys from two services:

### OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up or log in to your account
3. Navigate to the API section
4. Generate a new API key
5. Copy the API key

### DeepSeek API Key

1. Go to [DeepSeek](https://platform.deepseek.com/)
2. Create an account or sign in
3. Go to your profile settings
4. Generate a new API key
5. Copy the API key

## Configuration

1. Create a `.env` file in the project root:

   ```bash
   cp .env.example .env
   ```

2. Add your API keys to the `.env` file:
   ```
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   ```

## Usage

1. Make sure your virtual environment is activated
2. Run the main script:
   ```bash
   python main.py
   ```
3. Enter your question when prompted
4. Choose your preferred model (GPT-3.5 or Llama 3.2 1B)
5. View the detailed reasoning process and final answer

## Example

```
🤖 Reasoning is all you need 🤖

┌── Question
└─→ Why is the sky blue?

Select Model:
1. GPT 3.5
2. Llama 3.2 1B
Enter choice (1/2): 1

[Displays reasoning process and final answer]
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
