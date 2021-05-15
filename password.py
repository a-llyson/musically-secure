import random
import string

notes = 'CDEFGAB1234567'
pitch = '#b'
octave_dot = 'oO' # upper case O is upper octave while lower case o is lower octave
    # example: C#4bGBb17o  -> C# Fb G Bb C B(lower octave) -> notes should be played

note_convert = {
    "1": "C",
    "2": "D",
    "3": "E",
    "4": "F",
    "5": "G",
    "6": "A",
    "7": "B"
}

pitch_convert = {
    "Cb": "B",
    "Fb": "E",
    "B#": "C",
    "E#": "F"
}


# converts notes into notes that the synth can read
def converter(note):
    converted_note = ''
    numbers = '1234567'
    for i in range(0, len(note)):
        val = note[i]
        
        if val in numbers:
            converted_note = note_convert.get(val)
            print(converted_note)
#            converted_note = note_convert(val)
        elif val == '#' or val == 'b':
            converted_note += val
            if pitch_convert.get(converted_note) == None:
                converted_note = converted_note
            else:
                converted_note = pitch_convert.get(converted_note)
            print(converted_note)
 #           converted_note = pitch_convert(converted_note)
        elif val == 'o':
            converted_note += '3'
        elif val == 'O':
            converted_note += '5'
        else:
            converted_note = val

    if converted_note[-1] != '3' and converted_note[-1] != '5':
        converted_note += '4'
    
    return converted_note

def password_gen(num_pass=1, pass_len=1):
    number_of_passwords = num_pass
    password_length = pass_len

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

    return password_list

def note_password_gen(pass_list):
    all_password_sound = []
    single_password_sound = []

    # separates password into notes
    for i in pass_list:
        single_note = ''
        for letter in i:
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

    return all_password_sound

def convert_all(list_of_passwords):
    all_password_sound = []
    single_password_sound = []
    for i in list_of_passwords:
        for k in i:
            single_password_sound.append(converter(k))
        
        all_password_sound.append(single_password_sound)
        single_password_sound = []
    return all_password_sound


x = password_gen(2, 5)
y = note_password_gen(x)
z = convert_all(y)

print(x)
print(y)
print(z)
