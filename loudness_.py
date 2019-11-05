import soundfile as sf
import pyloudnorm as pyln


def main():
    data, rate = sf.read(filename)
    meter = pyln.Meter(rate)
    loudness = meter.integrated_loudness(data)
    print(filename," | loudness value :",loudness)
		

if __name__ == '__main__':
    filename = input("input file name : ")
    main()
