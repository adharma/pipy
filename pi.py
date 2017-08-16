from timer import slee
from multiprocessing import Pool

def start_function_for_processing(n):
	sleep(0.5)
	result_sent_back_to_parent = n * n
	return result_sent_back_to_parent

if __name__ == '__main__':
	with Pool(process=5) as p:
		results = p.map(start_function_for_processing, range(200), chunksize=10)
	print results