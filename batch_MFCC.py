import soundfile as sf
import pyloudnorm as pyln
import os
import librosa


def main():
	result_file = open('results/MFCC_'+Src+".txt", 'w')
	for filename in os.listdir(Src):
		waveform, sampling_rate = librosa.load(Src+'/'+filename)
		hop_length = 512
		tempo, beat_frames = librosa.beat.beat_track(y = waveform, sr = sampling_rate)	
		mfcc = librosa.feature.mfcc(y = waveform, sr = sampling_rate, hop_length = hop_length, n_mfcc=13)
		source_file = str(filename)
		mfcc_value =str(mfcc)
		result_file.write(source_file +" "+mfcc_value+'\n')
		print(filename," MFCC -> ", mfcc)
		

path = "results"
if os.path.exists(path)==False:
    os.mkdir(path)
if __name__ == '__main__':
    Src = input("Folder Name : ")
    main()
