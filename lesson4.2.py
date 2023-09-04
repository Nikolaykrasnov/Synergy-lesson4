number = int(input())
units = number % 10
dozens = number % 100 // 10
hundreds = number % 1000 // 100
thousands = number % 10000 // 1000
tens_of_thousands = number % 100000 //10000
print(((dozens ** units) * hundreds) // (tens_of_thousands - thousands))