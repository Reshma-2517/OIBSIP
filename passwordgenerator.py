import random 
import string

letters = string.ascii_letters
numbers = string.digits
special_chars = '!@#$%^&*()_~'


def random_password(spl_charlength, alpha_length, num_length):
    password_list = []
    password_list = ([random.choice(special_chars) for _ in range(spl_charlength)] +
                     [random.choice(numbers) for _ in range(num_length)] +
                     [random.choice(letters) for _ in range(alpha_length)] )

    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
try:
    special_chars_length = int(input('How many special characters you want to include in your password? '))
    alphabet_length = int(input('How many alphabet you want to include in your password? '))
    numbers_length = int(input('How many numbers you want to use in your password? '))
    total_length = special_chars_length + alphabet_length + numbers_length
    if total_length < 6:
        print('Password too short! Use atleast 6 caracters')
    else:
        final_password = random_password(spl_charlength=special_chars_length,alpha_length=alphabet_length,num_length=numbers_length)
        print(final_password)
except ValueError:
    print('Invalid input.Please type in the numerical values.')
