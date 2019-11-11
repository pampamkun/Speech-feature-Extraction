import numpy as np
import soundfile as sf
import pyloudnorm as pyln
import os
import librosa
import matplotlib.pyplot as plt
import sys
import numpy
import xlsxwriter
from tqdm import tqdm
numpy.set_printoptions(threshold=sys.maxsize)
def main():
	col = 0
	row = 0
	result_file = open(path+'/MFCC_'+Src+".txt", 'w')
	for filename in tqdm(os.listdir(Src)):
		min_list = []
		max_list = []
		name,ext = os.path.splitext(filename)
		str_name = str(name)
		waveform, sampling_rate = librosa.load(Src+'/'+filename)
		hop_length = 512
		kfcmfcc = librosa.feature.mfcc(y = waveform, sr = sampling_rate, hop_length = hop_length, n_mfcc=13)	
		for data in kfcmfcc:
				minx = data.min()
				maxx = data.max()
				min_list.append(minx)
				max_list.append(maxx)
		
		minmax_f = min_list+max_list
		worksheet.write_row(col, row, minmax_f)
		col+=1
		source_file = str(filename)
		mfcc_value_min =str(min_list)
		mfcc_value_max = str(max_list)
		result_file.write(source_file +" "+mfcc_value_min+mfcc_value_max+'\n')


if __name__ == '__main__':
    Src = input("Dataset Folder : ")
    path = input("Destinated Folder : ")
    if os.path.exists(path)==False:
    		os.mkdir(path)
		
    workbook = xlsxwriter.Workbook(path+"/"+"MFCC"+'.xlsx')
    worksheet = workbook.add_worksheet()
    main()
workbook.close()