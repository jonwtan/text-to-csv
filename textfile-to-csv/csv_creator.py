import csv
import re

output_file = "C:/Users/jwtan/Desktop/MelbDatathon2018/Melb & Regional Postcodes/vicpostcodes.csv"      #USER: Enter path of output file 

input_file = "C:/Users/jwtan/Desktop/MelbDatathon2018/Melb & Regional Postcodes/listofpostcodes.txt"	#USER: Enter path of input file


outfile = open(output_file, 'w')					# the .csv output file we want to make
outfile.write("Postcode , Suburb \n")				# writes in the header for the csv

infile = open(input_file, 'r')						# reads the input file of postcodes in VIC


for a in infile:
    
    b = re.findall("\w+", a)   
	
    outfile.write("%s, " % b[0])					# writes in postcode & a comma to output .csv
    
    n = 1											# writes suburb name to .csv . The code handles suburbs wt >1 word, eg. 'Glen Iris'
    while n < len(b):
        outfile.write("%s " % b[n])
        n += 1
	
    outfile.write("\n")


infile.close()
outfile.close()

