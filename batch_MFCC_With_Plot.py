import soundfile as sf
import pyloudnorm as pyln
import os
import librosa
import matplotlib.pyplot as plt
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)


def main():
	result_file = open('results/MFCC_'+Src+".txt", 'w')
	i = 0
	for filename in os.listdir(Src):
		name,ext = os.path.splitext(filename)
		str_name = str(name)
		waveform, sampling_rate = librosa.load(Src+'/'+filename)
		hop_length = 512
		tempo, beat_frames = librosa.beat.beat_track(y = waveform, sr = sampling_rate)	
		mfcc = librosa.feature.mfcc(y = waveform, sr = sampling_rate, hop_length = hop_length, n_mfcc=13)
		source_file = str(filename)
		mfcc_value =str(mfcc)
		result_file.write(source_file +" "+mfcc_value+'\n')
		i+=1
		print(i)
#		print(filename," MFCC -> ", mfcc)
		plt.plot(mfcc)
		plt.ylabel('mfcc')
		plt.savefig("results/"+str_name+'.png', dpi=1000)

path = "results"
if os.path.exists(path)==False:
    os.mkdir(path)
if __name__ == '__main__':
    Src = input("Folder Name : ")
    main()
