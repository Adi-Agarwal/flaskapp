from scipy.io import wavfile
import parselmouth as ps
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

def draw_pitch(pitch):
    # Extract selected pitch contour, and
    # replace unvoiced samples by NaN to not plot
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=5, color='w')
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=2)
    plt.grid(False)
    plt.ylim(0, pitch.ceiling)
    plt.ylabel("fundamental frequency [Hz]")
    plt.show()

def main():
    sample_rate, audio = wavfile.read("audios/C-note.wav")
    snd = ps.Sound("audios/C-note.wav")
    pitch = snd.to_pitch()
    frequencies = pitch.selected_array['frequency'] # Extract the pitch frequencies

if __name__ == "__main__":
    main()