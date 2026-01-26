# GPT Dating Assistant Telegram Bot

An AI-powered Telegram bot written in Python that assists users with social interactions, primarily focused on dating apps like Tinder. It uses a custom GPT service to generate profile texts, opening lines, conversation responses, and even simulate chats with celebrity personalities.

## 🌟 Features

This bot is designed to handle different stages of the online dating experience:

### 👤 Tinder Profile Generator (`/profile`)

A multi-step dialogue that collects user information (age, occupation, hobbies, pet peeves, goals) and then uses the GPT model to generate a compelling and engaging Tinder profile bio.

### 💖 Opener Message Creator (`/opener`)

Generates a creative and personalized first message based on information about the match (name, age, appearance rating, job, goal of dating).

### 💬 Conversation Assistant (`/message`)

Helps the user maintain a conversation by suggesting the next message, or even a message to invite the person on a date, based on the current chat history.

### 🔥 Celebrity Dating Simulator (`/date`)

Allows the user to engage in a simulated chat with a famous personality (e.g., Ariana Grande, Margot Robbie, Ryan Gosling). The AI adopts the persona of the celebrity, providing a fun and risk-free way to practice conversational skills.

### 🧠 General GPT Chat (`/gpt`)

A direct interface to ask the underlying GPT model any general question.

---

## ⚙️ Technologies

*   **Python 3.x**
*   **`python-telegram-bot`** (`telegram.ext` for handlers and application management)
*   **External GPT Service:** Utilizes a custom `ChatGptService` (from `gpt.py`) for all AI interactions, requiring an external API key (e.g., OpenAI or a similar LLM provider).
*   **Helper Functions:** Relies on custom utilities (`util.py`) for file loading (`load_message`, `load_prompt`), photo sending (`send_photo`), and custom dialogue management (`Dialog` class).

## 🚀 Setup and Installation

### Prerequisites

1.  **Python 3.x** installed.
2.  A **Telegram Bot Token** from BotFather.
3.  An **API Key** for the GPT service (e.g., OpenAI API Key).
4.  Required external files (`gpt.py`, `util.py`, and resources like images and message/prompt files).

### Installation Steps

1.  **Clone the repository:**

    ```bash
    git clone <your_repo_link>
    cd gpt-dating-assistant
    ```

2.  **Install the required library:**

    ```bash
    pip install python-telegram-bot
    ```

3.  **Configure API Keys:**

    Open the main script and replace the placeholder tokens with your actual keys:

    ```python
    # main script
    chatgpt = ChatGptService(token='YOUR_GPT_TOKEN') # Replace '111111111'
    app = ApplicationBuilder().token("YOUR_TELEGRAM_TOKEN").build() # Replace '11111111111'
    ```

4.  **Ensure Resources are Available:**

    Make sure the files for the prompts (`load_prompt`), messages (`load_message`), and images (`send_photo`) are correctly set up and accessible by the `util.py` functions, as the bot relies heavily on them.

5.  **Run the bot:**

    ```bash
    python bot.py
    ```

## 📚 Usage (Commands)

Start a chat with your bot and use the following commands:

| Command | Description | Handler |
| :--- | :--- | :--- |
| `/start` | Displays the main menu and available features. | `start` |
| `/profile` | Launches the Tinder profile generation dialogue. | `profile` |
| `/opener` | Launches the dialogue for generating a first message. | `opener` |
| `/message` | Accesses the conversation assistant features. | `message` |
| `/date` | Starts the celebrity dating simulation menu. | `date` |
| `/gpt` | Opens the general GPT chat mode for any question. | `gpt` |

---

### **Dialogue Flow**

Most features (`/profile`, `/opener`) involve a multi-step question-and-answer process handled by the `hello` message handler, which redirects based on the current `dialog.node`.
