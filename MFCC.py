import soundfile as sf
import pyloudnorm as pyln
import os
import librosa
import matplotlib.pyplot as plt

def main():
	result_file = open('results/MFCC'+fname+".txt", 'w')
	waveform, sampling_rate = librosa.load(fname)
	hop_length = 512
	tempo, beat_frames = librosa.beat.beat_track(y = waveform, sr = sampling_rate)	
	mfcc = librosa.feature.mfcc(y = waveform, sr = sampling_rate, hop_length = hop_length, n_mfcc=13)
	source_file = str(fname)
	mfcc_value =str(mfcc)
	result_file.write(source_file +" "+mfcc_value+'\n')
	print(fname," MFCC -> ", mfcc)
	plt.plot(mfcc)
	plt.ylabel('mfcc')
	plt.show()
		
path = "results"
if os.path.exists(path)==False:
    os.mkdir(path)
if __name__ == '__main__':
    fname = input("Filename.wav : ")
    print(fname)
    main()
