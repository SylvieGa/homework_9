print("Hey, it's time to play Fizzbuzz!")

end = input("Please enter a number between 1 and 100: ")
end = int(end)  # string into number

for num in range(1, end+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)