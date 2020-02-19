"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность
выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.
"""
revenue = int(input('Выручка ООО "Рога и Копыта" за отчетный период: '))
costs = int(input('Расходы ООО "Рога и Копыта" за отчетный период: '))

if revenue > costs:
    print('Фирма отработла с прибылью')
    print('Рентабельность', (revenue - costs) / revenue)
    number_employees = int(input('Численность сотрудников фирмы? '))
    print('Каждый сотрудник фирмы принес прибыль - ', (revenue - costs) / number_employees)
elif revenue == costs:
    print('Ваша фирма еще на плаву, но денег Вы не заработали')

else:
    print('Увы, Ваша фирма БАНКРОТ')
