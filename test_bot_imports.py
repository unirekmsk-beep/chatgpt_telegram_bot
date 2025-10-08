import time
print("=== BOT IMPORTS TEST STARTED ===")

try:
    print("1. Importing basic modules...")
    import logging
    import asyncio
    print("✅ Basic modules imported")
    
    print("2. Importing telegram...")
    from telegram.ext import Application
    print("✅ Telegram imported")
    
    print("3. Importing config...")
    import bot.config as config
    print("✅ Config imported")
    
    print("4. Testing bot import...")
    from bot.bot import run_bot
    print("✅ Bot imported successfully!")
    
    print("🎉 ALL IMPORTS WORK!")
    print("Bot should start normally now")
    
    # Запускаем бота
    print("🚀 Starting bot...")
    run_bot()
    
except Exception as e:
    print(f"❌ IMPORT ERROR: {e}")
    import traceback
    traceback.print_exc()

print("=== TEST FINISHED ===")
time.sleep(10)
