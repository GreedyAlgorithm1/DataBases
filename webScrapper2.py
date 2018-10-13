import urllib.request
import sys

def get_url(url, file_name):
	file_name = file_name + '.txt'
	file = open(file_name, 'w')
	url = url
	for line in urllib.request.urlopen(url):
		line = line.decode('utf-8').rsplit()
		name = line[0]
		file.write(name + '\n')
		#print(line)
	file.close()


def main():
	url = sys.argv[1]
	file_name = sys.argv[2]
	get_url(url, file_name)

main()
