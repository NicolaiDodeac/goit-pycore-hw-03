import random

#! варіант 2 відкорегований

def get_numbers_ticket(min: int, max: int, quantity:int) -> list:
    if min < 1 or max > 1000 or min > max or quantity > (max - min + 1):
        return []
    else:
        numbers_population = list(range(min,max + 1)) 
        unique_numbers = random.sample(numbers_population, quantity)
        return sorted(unique_numbers)
    
lottery_numbers = get_numbers_ticket(4, 98, 33)
print("Ваші лотерейні числа:", lottery_numbers)


#! варіант 1
# def get_numbers_ticket(min: int, max: int, quantity:int) -> list:
#     if min < 1 or max > 1000:
#         return []
#     elif not min % 1 ==0 or not max % 1 ==0:
#         return []
#     else:
#         numbers_population = []
#         while min <= max:
#             numbers_population.append(min)
#             min += 1
#         unique_numbers = random.sample(numbers_population, quantity)
#     return unique_numbers

# lottery_numbers = get_numbers_ticket(1, 498, 6)
# print("Ваші лотерейні числа:", lottery_numbers)

