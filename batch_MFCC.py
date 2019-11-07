import soundfile as sf
import pyloudnorm as pyln
import os
import librosa
from tqdm import tqdm


def main():
	result_file = open('results/MFCC_'+Src+".txt", 'w')
	for filename in tqdm(os.listdir(Src)):
		waveform, sampling_rate = librosa.load(Src+'/'+filename)
		hop_length = 512
		tempo, beat_frames = librosa.beat.beat_track(y = waveform, sr = sampling_rate)	
		mfcc = librosa.feature.mfcc(y = waveform, sr = sampling_rate, hop_length = hop_length, n_mfcc=13)
		source_file = str(filename)
		mfcc_value =str(mfcc)
		result_file.write(source_file +" "+mfcc_value+'\n')
		

numpy.set_printoptions(threshold=sys.maxsize)
path = "results"
if os.path.exists(path)==False:
    os.mkdir(path)
if __name__ == '__main__':
    Src = input("Folder Name : ")
    main()
