# -*- coding: utf-8 -*-
input_file = './a.txt'
output_file = './b.txt'

with open(output_file, "w") as aim:
    with open(input_file,"r") as file:
	    for line in file.readlines():
	    	if line.startswith('from'):
	    	    aim.write(line)