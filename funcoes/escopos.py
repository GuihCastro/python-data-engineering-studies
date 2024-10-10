salary = 4000
list = [1]

def salary_bonus(bonus, list):
    global salary

    aux_list = list.copy()
    aux_list.append(2)
    print(f"Lista auxiliar: {aux_list}")

    salary += bonus
    return salary

salary_with_bonus = salary_bonus(500, list)
print(salary_with_bonus)
print(list)