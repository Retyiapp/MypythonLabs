import math

salary = 5000
spend = 6000
months = 10
increase = 0.03

money_capital = 0
for i in range(months):
    money_capital += spend*(((increase+1)**i)) - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(money_capital))
