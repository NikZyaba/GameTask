class Game:  # Parent cls

    def __init__(self, noofquestion=0):
        self._noofauestion = noofquestion

    @property
    def noofquestion(self):
        return self._noofauestion

    @noofquestion.setter
    def noofquestion(self, value):  # Set questions count (from 1 to 10 (including))
        if value < 1:
            self._noofauestion = 1
            print(f'Minimum number of questions = 1. Hence, number of questions will be set to 1.')
        elif value > 10:
            self._noofauestion = 10
            print(f'Maximum number of question = 10. Hence, number of questions will be set to 10.')
        self._noofauestion = value


class BinaryGame(Game):
    def generate_questions(self):  # Random generator of questions (convertation from decimal to binary)
        from random import randint
        score = 0
        for i in range(self.noofquestion):
            base10 = randint(1, 100)
            user_result = input(f'Please convert: "{base10}" - to binary ')
            while True:
                try:
                    answer = int(user_result, base=2)
                    if answer == base10:
                        score += 1
                        print('AWESOME. You get 1 point')
                        break
                    else:
                        print('The answer is WRONG. The CORRECT answer is {:b}'.format(base10))
                        break
                except:
                    print(f'You did not enter a binary number. Please try again')
                    user_result = input(f'Please convert: "{base10}" - to binary ')

        return score


class MathGame(Game):

    def generate_questions(self):
        from random import randint
        score = 0
        number_list = [0, 0, 0, 0, 0]
        symbol_list = [' ', ' ', ' ', ' ', ' ']
        operator_dict = {1: '+', 2: '-', 3: '*', 4: '**'}
        for i in range(self._noofauestion):
            for index in range(0, 5):
                number_list[index] = randint(1, 9)
            for index in range(0, 4):
                if index > 0 and symbol_list[index - 1] == '**':
                    symbol_list[index] = operator_dict[randint(1, 3)]
                else:
                    symbol_list[index] = operator_dict[randint(1, 4)]

            question_string = str(number_list[0])
            for index in range(0, 4):
                question_string = question_string + symbol_list[index] + str(number_list[index + 1])

            result = eval(question_string)
            question_string = question_string.replace('**', '^')
            user_result = input(f'Calculate the value ({question_string})')

            while True:
                try:
                    answer = int(user_result)
                    if answer == result:
                        print('AWESOME, it is correct')
                        score += 1
                        break
                    else:
                        print(f'WRONG. Correct answer is {result}')
                        break
                except:
                    print('You did not enter a valid number. Please try again.')
                    user_result = input(f'Calculate the value ({question_string})')

            return score
