import traceback
import sys
from main import main

if __name__ == '__main__':
    try:
        # Пытаемся запустить главную функцию из main.py
        main()
    except Exception as e:
        # Если произошла любая ошибка — пишем ее в файл error.log
        with open('error.log', 'w') as f:
            f.write("Exception occurred:\n")
            f.write(str(e))
            f.write("\n\nTraceback:\n")
            traceback.print_exc(file=f)
        # Печатаем ошибку в консоль (на случай, если это увидит Timeweb)
        print("Error occurred, check error.log file")
        traceback.print_exc()
        # Завершаем работу с кодом ошибки 1
        sys.exit(1)
