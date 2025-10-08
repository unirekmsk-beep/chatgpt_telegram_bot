python
print("=" * 50)
print("🧪 TEST BOT STARTING")
print("=" * 50)

try:
    # Тест импортов
    import sys
    import os
    sys.path.append(os.path.dirname(__file__))
    
    print("📦 Testing imports...")
    import config
    print("✅ Config imported")
    
    # Тест конфига
    print(f"🔑 Token: {config.telegram_token[:10]}...")
    print(f"🔑 OpenAI: {config.openai_api_key[:10]}...")
    print(f"🗄️ MongoDB: {config.MONGODB_URI[:50]}...")
    
    # Тест базы данных (ОТДЕЛЬНО)
    print("🔄 Testing database...")
    from bot.database import Database
    try:
        db = Database()
        print("✅ Database connected!")
    except Exception as e:
        print(f"❌ Database failed: {e}")
        print("⚠️ Continuing without database...")
    
    # Тест бота
    print("🤖 Testing bot startup...")
    from bot.bot import run_bot
    print("✅ Bot imported successfully!")
    
    # Запуск
    print("🎉 STARTING BOT...")
    run_bot()
    
except Exception as e:
    print(f"💥 CRITICAL ERROR: {e}")
    import traceback
    traceback.print_exc()
    print("=" * 50)
