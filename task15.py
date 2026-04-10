import time

print("Загрузка: [          ] 0%", end="", flush=True)

for i in range(1, 11):
    time.sleep(1)
    
    filled = "#" * i
    empty = " " * (10 - i)
    
    print(f"\rЗагрузка: [{filled}{empty}] {i * 10}%", end="", flush=True)

print()