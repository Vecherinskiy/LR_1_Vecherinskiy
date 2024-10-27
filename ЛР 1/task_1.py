numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0
# TODO заменить значение пропущенного элемента средним арифметическим
len_numbers = len(numbers)
avg_numbers = sum(numbers) / len_numbers
new_numbers = numbers
new_numbers[4] = avg_numbers
print("Измененный список:", new_numbers)
