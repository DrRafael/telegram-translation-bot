# Telegram Translation & Text Analysis Bot

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![pyTelegramBotAPI](https://img.shields.io/badge/TelegramBotAPI-4.12%2B-blue.svg)](https://github.com/eternnoir/pyTelegramBotAPI)

A Telegram Bot that provides real-time text translation, session state memory management, and interactive inline button responses for user queries.

---

## 🚀 Key Features

* **Real-Time Translation**: Multi-language text translation API integration (`translate` library).
* **OOP Session State Storage**: Tracks user interaction history using Python `defaultdict` data structures.
* **Interactive Inline Keyboards**: Dynamic `InlineKeyboardMarkup` interface for user action handling.
* **Asynchronous Polling**: Resilient polling loop execution.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Framework**: pyTelegramBotAPI
* **Translation Engine**: Translate Library

---

## ⚙️ Configuration & Setup

### 1. Clone the repository
git clone https://github.com/DrRafael/telegram-translation-bot.git
cd telegram-translation-bot

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure API Credentials
Copy `config.py.example` to `config.py` and insert your Bot Token:
```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
