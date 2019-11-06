import soundfile as sf
import pyloudnorm as pyln
import os
import librosa
import matplotlib.pyplot as plt
import sys
import numpy
import xlsxwriter
numpy.set_printoptions(threshold=sys.maxsize)


def main():

	result_file = open(path+'/MFCC_'+Src+".txt", 'w')
	i = 0
	row = 0
	col = 0
	for filename in os.listdir(Src):
		name,ext = os.path.splitext(filename)
		str_name = str(name)
		waveform, sampling_rate = librosa.load(Src+'/'+filename)
		hop_length = 1024
		tempo, beat_frames = librosa.beat.beat_track(y = waveform, sr = sampling_rate)	
		mfcc = librosa.feature.mfcc(y = waveform, sr = sampling_rate, hop_length = hop_length, n_mfcc=13)
		for row, data in enumerate(mfcc):
			worksheet.write_row(col, row, data)
		col+=1
		source_file = str(filename)
		mfcc_value =str(mfcc)
		result_file.write(source_file +" "+mfcc_value+'\n')
		i+=1
		print("col =",col)
	#	print(filename," MFCC -> ", mfcc)
		plt.plot(mfcc)
		plt.ylabel('mfcc')
		plt.savefig(path+"/"+str_name+'.png', dpi=1000)

path = input("Destination Folder : ")
if os.path.exists(path)==False:
		os.mkdir(path)
		
workbook = xlsxwriter.Workbook(path+"/"+"MFCC"+'.xlsx')
worksheet = workbook.add_worksheet()

if __name__ == '__main__':
    Src = input("Folder Name : ")
    main()
workbook.close()
