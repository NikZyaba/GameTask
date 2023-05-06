from os import remove, rename


def print_instruction(instruction):
    print(instruction)


def get_user_score(user_name):
    try:
        with open('userScrores.txt', 'r') as file_scores:  # Open file if file was created \n
            # file for saving scores. File saving only {name},{score}
            for line in file_scores.readlines():  # Read all lines
                content = line.split(', ')  # Save line in list with name 'content'
                if content[0] == user_name:  # if name is in list 'content'
                    file_scores.close()  # close file
                    return content[1]  # return first 'score' from list
            return '-1'
    except IOError:
        print('File not found. A new file will be created')  # if file is not found program print this message
        file_scores = open('userScrores.txt', 'w')  # Create new file with name 'userScrores.txt'
        file_scores.close()  # Close file
        return '-1'


def update_user_score(new_user: bool, user_name, score):  # This fucntion for updating name and scores in file
    if new_user is True:
        file = open('userScrores.txt', 'a')
        file.write(f'\n{user_name}, {score}\n')
        file.close()
    else:
        temp = open('userScrores.tmp', 'w')  # Create new temporary file
        file = open('userScrores.txt', 'r')  # Open existing file
        for line in file.readlines():
            content = line.split(', ')
            if content[0] == user_name:
                score = content[1]
                temp.write(f'{user_name}, {score}\n')
            else:
                temp.write(line)

        temp.close()
        file.close()

        remove('userScrores.txt')
        rename('userScrores.tmp', 'userScrores.txt')
