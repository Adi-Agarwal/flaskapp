from scipy.io import wavfile
import crepe

def main():
    sample_rate, audio = wavfile.read("audios/C-scale.wav")
    time, frequency, confidence, activation = crepe.predict(audio, sample_rate, viterbi=True)

if __name__ == "__main__":
    main()