import random
import string

number_of_passwords = 3
password_length = 10
# password_length = int(input('How long should the password be? '))
# minimum length of 3

notes = 'CDEFGAB1234567'
pitch = '#b'
octave_dot = 'oO' # upper case O is upper octave while lower case o is lower octave
# example: C#4bGBb17o  -> C# Fb G Bb C B(lower octave) -> notes should be played


password_list = []
# Generate the passwords 
for i in range(number_of_passwords):
    password = ''
    current_length = 0
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

all_password_sound = []
single_password_sound = []

# separates password into notes
for i in range(number_of_passwords):
    print(password_list)
    single_note = ''
    new_note = True
    for letter in password_list[i]:
        if letter in notes:
            if single_note != '':
                single_password_sound.append(single_note)
            single_note = letter
        else:
            single_note += letter

    if single_note != '':
        single_password_sound.append(single_note)

    all_password_sound.append(single_password_sound)    
    single_password_sound = []

print(all_password_sound)


def note_convert(num):
    if num == '1':
        return 'C'
    elif num == '2':
        return 'D'
    elif num == '3':
        return 'E'
    elif num == '4':
        return 'F'
    elif num == '5':
        return 'G'
    elif num == '6':
        return 'A'
    elif num == '7':
        return 'B'

def pitch_convert(note):
    if note == 'Cb' : 
        return 'B'
    elif note == 'Fb':
        return 'E'
    elif note == 'B#': 
        return 'C'
    elif note == 'E#':
        return 'F'
    else:
        return note
# converts notes into notes that the synth can read



def converter(note):
    converted_note = ''
    numbers = '1234567'
    for i in range(0, len(note)):
        val = note[i]
        converted_note = val
        if val in numbers:
            converted_note = note_convert(val)
        elif val == '#' or val == 'b':
            converted_note += val
            converted_note = pitch_convert(converted_note)
        if val == 'o':
            converted_note += '3'
        elif val == 'O':
            converted_note += '5'

    print('115')
    print(converted_note)
    if converted_note[-1] != '3' or converted_note[-1] != '5':
        converted_note += '4'
    
    return converted_note

print(converter('C#'))