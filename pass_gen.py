import random
import string
from ask_user import *



def password_gen():
   
 
    if question_2 == 1:
        gen1 = string.ascii_letters
        random1 = random(gen1, k= question_1)
        password = "".join(random1)
        print(f"Your password is: {password}")
    elif question_2 == 2:
        gen2 = string.hexdigits
        random2 = random.choices(gen2, k= question_1)
        password = "".join(random2)
        print(f"YOur password is: {password}")
    elif question_2 == 3:
        punc = string.punctuation
        stri = string.ascii_letters
        random_punc = random.choices(punc, k = question_1//2)
        random_stri = random.choices(stri, k = question_1//2)
        join_pns = random_punc + random_stri
        random3 = random.choices(join_pns, k= question_1)
        password ="".join(random3)
        print(f"Your password is: {password}")
    elif question_2 == 4:
        punc = string.punctuation
        num = string.digits
        random_punc = random.choices(punc, k = question_1//2)
        random_num = random.choices(num, k = question_1//2)
        join_pnn = random_punc + random_num
        random4 = random.choices(join_pnn, k= question_1)
        password ="".join(random4)
        print(f"Your password is: {password}")
    elif question_2 == 5:
        punc = string.punctuation
        num = string.digits
        stri = string.ascii_letters
        random_punc = random.choices(punc, k = question_1//2)
        random_num = random.choices(num, k = question_1//2)
        random_stri = random.choices(stri, k = question_1//3)
        join_pnn = random_punc + random_num + random_stri
        random5 = random.choices(join_pnn, k= question_1)
        password ="".join(random5)
        print(f"Your password is: {password}")








