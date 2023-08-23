import random


result = {'win': 0, 'lose': 0, 'tie': 0}

while True:
    try:
        input_choice = input('(가위/바위/보) 중 하나를 선택하세요: ')
        if input_choice != '가위' and input_choice != '바위' and input_choice != '보':
            raise ValueError

        option_list = ['가위', '바위', '보']
        random_choice = random.choice(option_list)

        if (input_choice == '가위' and random_choice == '보') or (input_choice == '바위' and random_choice == '가위') or (input_choice == '보' and random_choice == '바위'):
            print('Me: ', input_choice)
            print('Computer: ', random_choice)
            print('WIN!')
            result['win'] += 1

        if (input_choice == '가위' and random_choice == '바위') or (input_choice == '바위' and random_choice == '보') or (input_choice == '보' and random_choice == '가위'):
            print('Me: ', input_choice)
            print('Computer: ', random_choice)
            print('Lose..')
            result['lose'] += 1

        if input_choice == random_choice:
            print('Me: ', input_choice)
            print('Computer: ', random_choice)
            print('Tie')
            result['tie'] += 1

        answer = input('게임을 다시 하겠습니까(yes/no)?').upper()

        if answer == 'NO':
            print(result)
            print('Bye!')
            break
    except ValueError:
        print("Oops!!! '가위/바위/보' 중 입력해 주세요.")
