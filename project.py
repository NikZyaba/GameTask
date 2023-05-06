from gametask import print_instruction, \
    get_user_score, update_user_score
from gameclasses import MathGame, \
    BinaryGame

try:
    math_instructions = 'В этой игре Вам предлагается решить простую арифметическую задачу. ' \
                        'За каждый правильный ответ Вам начисляется одно очко.' \
                        'За ошибочные ответы очки не вычитаются.'

    binary_instructions = 'В этой игре Вы получаете десятичное число.' \
                          'Ваша задача - преобразовать его в двоичную систему исчисления' \
                          'За каждый правильный ответ Вам начисляется одно очко' \
                          'За ошибочные ответы очки не вычитаются'
    bg = BinaryGame()
    mg = MathGame()

    user_name = input('Enter your username: ')
    score = int(get_user_score(user_name))
    if score == -1:
        new_user = True
        score = 0
    else:
        new_user = False

    print(f'Hello {user_name}, welcome to the game')
    print(f'Your current score is {score}')

    userChoice = '0'

    while userChoice != '-1':
        game = input('Enter the number: "Binary game" is (1), "Math game" is (2): ')
        while game != '1' and game != '2':
            print('Please enter game. You need to choose 1 (one) or 2 (two).')
            game = input('Enter the number: "Binary game" is (1), "Math game" is (2): ')
        num_promt = input('How many question do you want to choose? (1 - 10) - ')
        while True:
            try:
                num = int(num_promt)
                break
            except:
                print('You did not enter a valid number. Please try again.')
                num_promt = input('How many question do you want to choose? (1 - 10) - ')

        if game == '2':
            mg.noofquestion = num
            print_instruction(math_instructions)
            score += mg.generate_questions()
        else:
            bg.noofquestion = num
            print_instruction(binary_instructions)
            score += bg.generate_questions()

        print(f'Your current score is {score}')
        userChoice = input('Press ENTER to continue or -1 to end: ')
    update_user_score(new_user, user_name, str(score))
except Exception as e:
    print('An unknown ERROR occured. Program will exit')
    print('Error:', e)
