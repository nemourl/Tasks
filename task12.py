total = 0

while True:
    price = float(input("Введите стоимость товара (0 для завершения): "))
    
    if price == 0:
        break
    
    if price < 0:
        print("Ошибка: стоимость не может быть отрицательной")
        continue
    
    total = total + price

print(f"Общая сумма покупки: {total} рублей")

if total > 5000:
    discount = total * 0.10  
    final_price = total - discount
    print(f"Скидка 10%: -{discount} рублей")
    print(f"Итоговая сумма со скидкой: {final_price} рублей")
elif 2000 <= total <= 5000:
    discount = total * 0.05 
    final_price = total - discount
    print(f"Скидка 5%: -{discount} рублей")
    print(f"Итоговая сумма со скидкой: {final_price} рублей")
else:
    print("Скидка не применяется")