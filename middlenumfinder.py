import random

def generate_random_number():
    min_val = int(input('enter min val'))
    max_val = int(input('Enter max val'))

    if min_val > max_val:
        print('Error min cannot exceed max val')
    else:
        
        random_number = random.randint(min_val, max_val)
        print('generated random number', random_number)
        print('the min and max values', min_val, max_val)
generate_random_number()
        
