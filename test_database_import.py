print("=== DATABASE IMPORT TEST ===")

import sys
import os
sys.path.append(os.path.dirname(__file__))

try:
    print("1. Testing import config...")
    import bot.config
    print("✅ bot.config imported")
    
    print("2. Testing import pymongo...") 
    import pymongo
    print("✅ pymongo imported")
    
    print("3. Testing import database module...")
    from bot import database
    print("✅ bot.database module imported")
    
    print("🎉 ALL IMPORTS SUCCESSFUL!")
    
except Exception as e:
    print(f"❌ IMPORT ERROR: {e}")
    import traceback
    traceback.print_exc()
