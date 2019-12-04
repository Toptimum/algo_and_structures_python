"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

N_ENTERPRISES = int(input("Сколько предприятий вы хотите добавить? "))

enterprises = {}
average_profit = 0

# создадим словарь компаний с их прибылью по кварталам
for i in range(N_ENTERPRISES):
    name_enterprise = input(f"Введите название {i + 1}-го предприятия: ")
    quarter_profit = []
    for j in range(4):  # всего 4 квартала в году
        profit = int(input(f"Введите прибыль предприятия за {j + 1}-й квартал: "))
        quarter_profit.append(profit)
        average_profit += profit
    enterprises[name_enterprise] = quarter_profit

# определим среднюю прибыль за год для всех предприятий
average_profit = average_profit / N_ENTERPRISES
print(f"\nСредняя прибыль всех предприятий за год составляет {average_profit} руб.")

# определим наименования предприятий, чья прибыль ниже среднего и отдельно, чья прибыль выше среднего
low_profit_companies = []
high_profit_companies = []

for name_company, profit_company in enterprises.items():
    sum_profit = 0
    for q in range(len(profit_company)):
        sum_profit += profit_company[q]
    if sum_profit < average_profit:
        low_profit_companies.append(name_company)
    else:
        high_profit_companies.append(name_company)
print(f"\nНаименования предприятий, чья прибыль ниже среднего: {low_profit_companies},\n"
      f"и предприятия, чья прибыль выше среднего: {high_profit_companies}.")
