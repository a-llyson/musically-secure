import random
import string

number_of_passwords = 3
password_length = 10
# password_length = int(input('How long should the password be? '))
# minimum length of 3

notes = 'CDEFGAB1234567'
pitch = '#b'
octave_dot = 'oO' # upper case O is upper octave while lower case o is lower octave
time_signature = '123456789'
slash = '/'
# example: 4/4C#4bGBb17o  -> time is 4/4, C# Fb G Bb C B(lower octave) -> notes should be played


password_list = []
# Generate the passwords 
for i in range(number_of_passwords):
    password = ''
    password += random.choice(time_signature) + slash + random.choice(time_signature)
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
    
    password_list.append(password)

print(password_list)

time_beat = []
all_password_sound = []
single_password_sound = []

# separates password into notes and time signature
for i in range(number_of_passwords):
    beat = password_list[i][:3]
    time_beat.append(beat)
   # print(time_beat)
    password_list[i]=password_list[i][3:]
    print(password_list)

    single_note = ''
    new_note = True
    for letter in password_list[i]:
        if letter in notes:
            if single_note != '':
                #print(single_note)
                single_password_sound.append(single_note)
            single_note = letter
        else:
            single_note += letter

    if single_note != '':
        single_password_sound.append(single_note)

    all_password_sound.append(single_password_sound)    
    single_password_sound = []

print(all_password_sound)
    


