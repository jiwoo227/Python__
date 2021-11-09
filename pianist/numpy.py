import numpy as np

samplerate = 44100  # Frequecy in Hz


def get_wave(freq, duration=0.5):
    '''
    Function takes the "frequecy" and "time_duration" for a wave
    as the input and returns a "numpy array" of values at all points
    in time
    '''

    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)

    return wave


# To get a 1 second long wave of frequency 440Hz
a_wave = get_wave(440, 1)

# wave features
print(len(a_wave))  # 44100
print(np.max(a_wave))  # 4096
print(np.min(a_wave))  # -4096