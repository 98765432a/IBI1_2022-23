import re
DNA='GGgATgcccccctgaAAAT'#an example, which is supposed to be protein-coding
#DNA=input('input a DNA sequence here:')#use this if we need to input DNA sequence
coding=DNA.upper()#change the DNA sequence into upper class
num_coding=len(coding)#calculate how many letters in the input DNA sequence
extract=str(re.findall(r'ATG(\S+)TGA',coding))#extract the coding sequence and change the type into string
num_extract=len(extract)#calculate how many letters in the input DNA sequence
def calculate(coding,extract):
	"""input num_coding,num_extract
	calculate the percentage of coding sequence
	print the percentage
	define the types of the DNA according to the percentage"""
	print('the coding part of this DNA is:')
	percentage=num_extract/num_coding#calculate how much percentage the coding sequence take place of the DNA sequence.
	print('{:.2%}'.format(percentage))#print out the percentage of coding part in the form of percentage
	if percentage>0.5:
		print('protein-coding')
	elif percentage<0.1:
		print('non-coding')
	else:
		print('unclear')
c=calculate(num_coding, num_extract)#input parameters
