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
    print(f"🗄️ MongoDB URI: {config.MONGODB_URI}")
    
    # ТЕСТ БАЗЫ ДАННЫХ С ДИАГНОСТИКОЙ
    print("🔄 Testing database connection...")
    try:
        import pymongo
        print("✅ PyMongo imported")
        
        # Тестируем подключение отдельно
        print("🔌 Attempting to connect to MongoDB...")
        client = pymongo.MongoClient(config.MONGODB_URI, serverSelectionTimeoutMS=5000)
        
        # Проверяем подключение
        print("📡 Checking connection...")
        client.admin.command('ismaster')
        print("✅ MongoDB connection successful!")
        
        # Проверяем базу данных
        db = client["default_db"]
        print("✅ Database accessed successfully")
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
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
