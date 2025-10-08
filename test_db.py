print("=== DATABASE CONNECTION TEST ===")

import sys
import os
sys.path.append(os.path.dirname(__file__))

try:
    from bot.database import Database
    print("✅ Database class imported")
    
    print("🔄 Testing connection...")
    db = Database()
    print("🎉 DATABASE CONNECTED SUCCESSFULLY!")
    
    # Тестируем базовые операции
    print("🧪 Testing basic operations...")
    result = db.check_if_user_exists(123)
    print(f"✅ check_if_user_exists: {result}")
    
    print("🎉 ALL DATABASE TESTS PASSED!")
    
except Exception as e:
    print(f"❌ DATABASE ERROR: {e}")
    import traceback
    traceback.print_exc()
