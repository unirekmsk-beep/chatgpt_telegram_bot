print("=" * 60)
print("🤖 ULTRA SIMPLE BOT STARTING - NO DATABASE")
print("=" * 60)

import os
import sys
import asyncio

# Добавляем текущую директорию в путь
sys.path.append(os.path.dirname(__file__))

try:
    # 1. БАЗОВЫЕ ИМПОРТЫ
    print("📦 Step 1: Testing basic imports...")
    import config
    print("✅ Config imported")
    
    # 2. ПРОВЕРКА КОНФИГА
    print("🔧 Step 2: Checking config...")
    print(f"   Token: {config.telegram_token[:10]}...")
    print(f"   OpenAI: {config.openai_api_key[:10]}...")
    
    # 3. ПРОПУСКАЕМ ВСЕ СЛОЖНЫЕ ИМПОРТЫ
    print("⏭️  Step 3: Skipping database and complex imports...")
    
    # 4. ЗАПУСКАЕМ ПРОСТЕЙШЕГО БОТА
    print("🚀 Step 4: Starting minimal bot...")
    
    from telegram.ext import Application, CommandHandler
    from telegram import Update
    from telegram.ext import ContextTypes
    
    # Простейший хендлер
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🎉 Bot is ALIVE! Database disabled for now.")
    
    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("ℹ️ This is a test version without database.")
    
    # Создаем и настраиваем приложение
    application = Application.builder().token(config.telegram_token).build()
    
    # Добавляем хендлеры
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    
    print("✅ Bot configured successfully")
    print("🎛️ Starting polling...")
    
    # Запускаем
    application.run_polling()
    
except ImportError as e:
    print(f"📦 IMPORT ERROR: {e}")
    import traceback
    traceback.print_exc()
    
except Exception as e:
    print(f"💥 RUNTIME ERROR: {e}")
    import traceback
    traceback.print_exc()

print("=" * 60)
