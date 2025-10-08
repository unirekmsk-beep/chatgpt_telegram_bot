import time
print("=== HEALTH CHECK STARTED ===")
print("✅ Python is running")
print("✅ Script is executing")

# Ждем 30 секунд чтобы проверить что контейнер стабилен
for i in range(30):
    print(f"⏰ Still running... {i+1}/30")
    time.sleep(1)

print("=== HEALTH CHECK COMPLETED ===")
