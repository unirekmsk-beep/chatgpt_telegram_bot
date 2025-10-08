print("=== SIMPLE TEST ===")

# Простейший тест без сложных импортов
try:
    import telegram
    print("✅ Telegram imported")
    
    # Создаем минимального бота
    from telegram.ext import Application, CommandHandler
    
    async def start(update, context):
        await update.message.reply_text("✅ Bot is working!")
    
    # Для теста - просто выводим сообщение
    print("✅ All basic imports work!")
    print("🎉 Test passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
