witnesses = int(input())
witnesses_numbers = [set(input()) for i in range(witnesses)]


def rate(c_number):
    k = 0
    for number in witnesses_numbers:
        if len(number - set(c_number)) == 0:
            k += 1
    return k


nums = int(input())
car_nums = {}
car_numbers = []
for j in range(nums):
    n = input()
    car_numbers.append(n)
    car_nums[n] = rate(n)

best_rate = max(car_nums.values())
print(*[n for n in car_numbers if car_nums[n] == best_rate], sep='\n')
