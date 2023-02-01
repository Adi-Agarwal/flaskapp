from scipy.io import wavfile
import matplotlib.pyplot as plt

import numpy as np
from IPython.display import clear_output
from scipy.fftpack import fft, fftshift
from scipy.signal import *
from sklearn.preprocessing import *

LOW_THRESHOLD = 2e-4;
HIGH_THRESHOLD = 0.7;
MUSIC_RANGE = [15, 8000];

NOTES = {
    261.63: 'C',
    277.18: 'C#',
    293.66: 'D',
    311.13: 'D#',
    329.63: 'E',
    349.23: 'F',
    369.99: 'F#',
    392.00: 'G',
    415.30: 'G#',
    440.00: 'A',
    466.16: 'A#',
    493.88: 'B'
}

def getFreq(start, end, sig):
    segment = sig[start:end];
    freq = np.abs(fft(segment));
    
    return np.mean(freq);

def getFirstNonzero(sig, starti):
    for i in range(starti, len(sig)):
        if sig[i] != 0:
            return i;

def findClosestKey(freq, d):
    keys = list(d.keys());
    for i in range(len(keys) - 1):
        if keys[i] < freq and keys[i+1] > freq:
            return keys[i];

    return keys[-1];

def getNotes(fileName):

   

    sample_rate, time_domain_sig = wavfile.read("audios/C-scale.wav");
    


    notes = [];
    frequencies = [];

    num_samples = len(time_domain_sig);
    clip_len = num_samples // sample_rate;
    onesec = sample_rate;

    time_ax = np.linspace(0, clip_len, num_samples);
    plt.subplot(2, 1, 1)
    plt.plot(time_ax, time_domain_sig);
    plt.xlim([0, 8]);

    print(time_domain_sig.shape)

    sixteenth = onesec // 4;
    f, t, Zxx = stft(time_domain_sig, fs=sample_rate, window = 'hann', nperseg = sixteenth, noverlap = sixteenth // 8);

    magZ = np.abs(Zxx);

    print(magZ.shape)
    print(f.shape)
    print(t.shape)
    print(np.amax(magZ));
    med = np.median(magZ);
    
    for i in range(len(f)):
        for j in range(len(t)):
            if (magZ[i][j] < med): magZ[i][j] = 0;

    plt.subplot(2, 1, 2)
    plt.pcolormesh(t, f, magZ, shading='gouraud')

    plt.title('STFT Magnitude')

    plt.ylabel('Frequency [Hz]')
    plt.ylim((0, 500));
    
    plt.xlabel('Time [sec]')

    plt.show()

    return {};
    for i in range(0, clip_len, sample_rate):
        if (i + sample_rate >= len(f)): break;
        avgFreq = np.mean(f[i:i+sample_rate]);
        frequencies.append(avgFreq);

    for freq in frequencies:
        print(freq)
        key = findClosestKey(freq, NOTES);
        notes.append(NOTES[key]);

    print(notes);
    return notes;



def main():
    getNotes("d");