import random
import string

number_of_passwords = 1
password_length = 10
# password_length = int(input('How long should the password be? '))
# minimum length of 3

notes = 'CDEFGAB1234567'
pitch = '#b'
octave_dot = 'oO' # upper case O is upper octave while lower case o is lower octave
time_signature = '123456789'
slash = '/'
# example: 4/4C#4bGBb17o  -> time is 4/4, C# Fb G Bb C B(lower octave) -> notes should be played


for i in range(number_of_passwords):
    password = ''
    password += random.choice(time_signature) + slash + random.choice(time_signature)
    print(password)
    current_length = 3
    while current_length < (password_length):
        sharp_flat = random.randint(0,1)
        octave = random.randint(0,1)
        password += random.choice(notes)
        current_length += 1

        if current_length >= password_length:
            break

        if sharp_flat == 0:
            password += random.choice(pitch)
            current_length += 1

        if current_length >= password_length:
            break
        
        if octave == 0:
            password += random.choice(octave_dot)
            current_length += 1
    
    print(password)



