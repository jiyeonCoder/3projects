import random

random_num = random.randint(1, 100)
count = 0
highest_count = 0
while True:
    try:
        input_num = int(input("Please enter a number(1-100): "))
        count += 1
        if input_num > random_num:
            print('Down')

        elif input_num < random_num:
            print('Up')

        else:
            if count >= highest_count:
                highest_count = count
            print('Great!')
            print('Current count: ', count)
            print('Highest count: ', highest_count)
            answer = input("Do you want to try again?(yes/no) ")
            if answer == 'yes':
                random_num = random.randint(1, 100)
                count = 0
            else:
                print('Bye!')
                break

    except ValueError:
        print("Oops!Type valid number. Try again...")
