import string 
import random

LETTER = string.ascii_letters
NUMBER = string.digits
PUNCTUATION = string.punctuation
def get_password_lenght():
    while True:
        try: 
            lenght = int(input('How long do you waint your password: '))
            return lenght
        except ValueError:
            print("The value you entered is not the number,please re-enter!!!")
        
    
        
def password_generator(length):
    printable = f'{LETTER}{NUMBER}{PUNCTUATION}'
    printable = list(LETTER)
    random.shuffle(printable)
    random_password = random.choices(printable,k=length)
    random_password = ''.join(random_password)
    return random_password

def main():
    lenth = get_password_lenght()
    password = password_generator(lenth)
    print(password)
    
if __name__ == '__main__':
    main()
    