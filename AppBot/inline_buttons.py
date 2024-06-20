from aiogram import types

web_app_button = types.WebAppInfo(url="https://f433-195-158-9-110.ngrok-free.app")
button_text = "Open Web App"
keyboard_button = types.KeyboardButton(text=button_text, web_app=web_app_button)
button_web_app = types.ReplyKeyboardMarkup(keyboard=[[keyboard_button]], resize_keyboard=True)
