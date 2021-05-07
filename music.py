from synthesizer import Player, Synthesizer, Waveform, Writer
from password import password_gen, note_password_gen, convert_all
import os
import glob
from pydub import AudioSegment


DIR = os.path.dirname(os.path.abspath(__file__))


def play_password(lop):
    i = 0
    k = 0
    combined_sounds = AudioSegment.empty()
    directory = "C:/Users/allys/Documents/Coding/vs/musically-secure"
    writer = Writer()
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    for password in lop:
        filename2 = "password" + str(k) + ".wav"
        for note in password:
 #          player.synthesizer.generate_constant_wave(note, 0.5)
            sound = synthesizer.generate_constant_wave(note, 0.5)
            name =  str(i) + "note" + ".wav"
            i += 1
            writer.write_waves(os.path.join(DIR, name), sound)
        for file in sorted(os.listdir(directory)):
            filename = os.path.join(directory,file)
            if filename.endswith("note.wav"):
                p1 = AudioSegment.from_wav(filename)
                combined_sounds += p1  
        combined_sounds.export(filename2, format="wav")
        k += 1
        combined_sounds = AudioSegment.empty()

        for file in sorted(os.listdir(directory)):
            filename = os.path.join(directory,file)
            if filename.endswith("note.wav"):
                os.remove(filename)

        

'''
x = password_gen(5, 5)
y = note_password_gen(x)
z = convert_all(y)
play_password(z)
'''