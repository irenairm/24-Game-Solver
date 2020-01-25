from back import *
from sys import argv


def environment(filename1,filename2):
	file = open(filename1,"r")
	read = [int(s) for s in file.read().split()] #mengubah string yang ada di file menjadi integer
	greedy = greedy24(read) #agar bisa dimasukkan ke dalam algoritma greedy
	
	file2 = open(filename2,"a+") #menambahkan hasil perhitungan ke dalam file
	greedy_str = str(greedy)
	file2.write(greedy_str)
	file2.close()

environment(argv[1],argv[2])
