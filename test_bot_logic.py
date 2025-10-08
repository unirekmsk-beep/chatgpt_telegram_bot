import time
import asyncio
print("=== BOT LOGIC TEST STARTED ===")

try:
    print("1. Importing bot...")
    from bot.bot import run_bot
    print("✅ Bot imported")
    
    print("2. Testing bot startup...")
    
    # Запускаем бота в отдельной таске с таймаутом
    async def test_bot():
        try:
            print("🔄 Starting bot...")
            await run_bot()
        except Exception as e:
            print(f"❌ Bot runtime error: {e}")
            import traceback
            traceback.print_exc()
    
    # Запускаем с таймаутом
    print("⏰ Running bot with timeout...")
    try:
        asyncio.run(asyncio.wait_for(test_bot(), timeout=10.0))
    except asyncio.TimeoutError:
        print("⏰ Bot timeout - might be running normally")
    except Exception as e:
        print(f"❌ Bot failed: {e}")
        import traceback
        traceback.print_exc()
    
    print("🎉 BOT LOGIC TEST COMPLETED")
    
except Exception as e:
    print(f"💥 CRITICAL ERROR: {e}")
    import traceback
    traceback.print_exc()

print("=== TEST FINISHED ===")
time.sleep(5)
