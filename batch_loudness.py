import soundfile as sf
import pyloudnorm as pyln
import os


def main():
	result_file = open('results/loudness_'+Src+".txt", 'w')
	for filename in os.listdir(Src):
		data, rate = sf.read(Src+'/'+filename)
		meter = pyln.Meter(rate)
		loudness = meter.integrated_loudness(data)
		loud_value = str(loudness)
		source_file = str(filename)
		result_file.write(source_file +" "+loud_value+'\n')
		print(filename, loudness)
		

path = "results"
if os.path.exists(path)==False:
    os.mkdir(path)
if __name__ == '__main__':
    Src = input("Folder Name : ")
    main()
