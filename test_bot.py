print("=" * 60)
print("🤖 TEST BOT STARTING")
print("=" * 60)

import os
import sys

# ✅ ПРАВИЛЬНЫЕ ПУТИ ДЛЯ ИМПОРТА
# Добавляем корневую директорию в Python path
sys.path.insert(0, os.path.dirname(__file__))

try:
    print("📦 Testing imports with correct paths...")
    
    # Теперь можем импортировать корректно
    from bot import config
    print("✅ bot.config imported")
    
    print(f"🔑 Token: {config.telegram_token[:10]}...")
    
    # Пробуем импортировать основной бот
    from bot.bot import run_bot
    print("✅ bot.bot imported")
    
    # Запускаем
    print("🎉 Starting main bot...")
    run_bot()
    
except Exception as e:
    print(f"💥 ERROR: {e}")
    import traceback
    traceback.print_exc()

print("=" * 60)
