import math
budget = float(input())
students = int(input())
pice_flour = float(input())
price_egg = float(input())
price_apron = float(input())


apron_percent = math.ceil(students * 1.2)
needed_item = price_apron * (apron_percent) + price_egg * 10 * (students) + pice_flour*(students-((students // 5)))
if needed_item <= budget:
    print(f"Items purchased for {needed_item:.2f}$.")
else:
    need = abs(budget - needed_item)
    print(f"{need:.2f}$ more needed.")