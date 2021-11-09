from pprint import pprint


def get_piano_notes():
    '''
    Returns a dict object for all the piano
    note's frequencies
    '''
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    base_freq = 261.63  # Frequency of Note C4

    note_freqs = {octave[i]: base_freq * pow(2, (i / 12)) for i in range(len(octave))}
    note_freqs[''] = 0.0  # silent note

    return note_freqs

    # To get the piano note's frequencies


note_freqs = get_piano_notes()
pprint(note_freqs)
'''
         {'': 0.0,
         'A': 440.00745824565865,
         'B': 493.8916728538229,
         'C': 261.63,
         'D': 293.66974569918125,
         'E': 329.63314428399565,
         'F': 349.2341510465061,
         'G': 392.0020805232462,
         'a': 466.1716632541139,
         'c': 277.18732937722245,
         'd': 311.1322574981619,
         'f': 370.00069432367286,
         'g': 415.31173722644}
'''