import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN
from logic import TextAnalysis

bot = telebot.TeleBot(TOKEN)


def build_text_action_keyboard() -> InlineKeyboardMarkup:
    """Generates inline action buttons for text processing options."""
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton('Get Assistant Response', callback_data='text_ans'),
        InlineKeyboardButton('Translate Message', callback_data='text_translate')
    )
    return markup


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    """Handles inline keyboard button clicks for translation and response actions."""
    if "text" in call.data:
        user_history = TextAnalysis.memory.get(call.from_user.username)
        
        if user_history:
            latest_analysis = user_history[-1]
            if call.data == "text_ans":
                bot.send_message(call.message.chat.id, latest_analysis.response)
            elif call.data == "text_translate":
                bot.send_message(call.message.chat.id, f"Translation:\n{latest_analysis.translation}")
        else:
            bot.send_message(call.message.chat.id, "No active text session found.")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Processes incoming text messages and presents action choices."""
    bot.send_chat_action(message.chat.id, 'typing')
    
    # Store analysis in memory
    username = message.from_user.username or str(message.from_user.id)
    TextAnalysis(message.text, username)
    
    response_text = "I received your message! Choose an action below:"
    bot.send_message(
        message.chat.id, 
        response_text, 
        reply_markup=build_text_action_keyboard()
    )


if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
