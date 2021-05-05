import numpy
import matplotlib.pyplot as mpl
from pprint import pprint

hertz = 44100

def get_wave(freq, duration=0.5):
    amplitude = 4096
    t = numpy.linspace(0, duration, int(hertz * duration))
    wave = amplitude * numpy.sin(2 * numpy.pi * freq * t)

    return wave

def get_piano_notes():
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    base_freq = 261.63

    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}
    note_freqs[''] = 0.0

    return note_freqs

a_wave = get_wave(440, 1)
'''
mpl.plot(a_wave[0:int(44100/440)])
mpl.xlabel('time')
mpl.ylabel('Amplitude')
mpl.show()
'''
note_freqs = get_piano_notes()
pprint(note_freqs)

