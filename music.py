from synthesizer import Player, Synthesizer, Waveform
from password import password_gen, note_password_gen, convert_all

x = password_gen(1, 15)
y = note_password_gen(x)
z = convert_all(y)
#print(z)

def play_password(lop):
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    '''
    notes = ['E4', 'D4', 'C4', 'D4', 'E4', 'E4', 'E4', 'D4', 'D4', 'D4', 'E4', 'G4', 'G4', 'E4', 'D4', 'C4', 'D4', 'E4', 'E4', 'E4', 'E4', 'D4', 'D4', 'E4', 'D4', 'C4']
    
    '''
    for password in lop:
        for note in password:
            player.play_wave(synthesizer.generate_constant_wave(note, 0.5))

play_password(z)