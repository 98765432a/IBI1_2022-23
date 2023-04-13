#find the line start with>
#extract the gene name
#other lines:gene sequence
#make the sequence from one gene in one line
#if the gene ends with TGA
#store this gene and its gene name into TGA_genes.fa

import re
f=open('/Users/wd/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')#open the file
#TGA=f.read()#read the file
out=open('/Users/wd/Desktop/IBI1_2022-23/Practical 9/TGA_genes.fa','w')#creat a file called TGA_genes.fa and open it with the permission of writing
separator=''#a parameter used to change list into string
for line in f:#read the file line by line
	if line.startswith('>'):#recognize line start with" >"
		line1=re.findall(r'^>\S+',line)#find gene name
		name=separator.join(line1)#line1 is a list, we need to change list into string so then out.write()can run
		sequence=''#define sequence
	else:
		line2=line.rstrip()#delete white space at the end of the line
		sequence += line2#add those gene sequence in several lines together
		if sequence.endswith('TGA'):#recognize sequence end with TGA
				out.write(name)#write gene name into TGA_genes1.fa
				out.write('\n'+sequence+'\n')#write gene sequence TGA_genes1.fa,nano count_cds_genes.py,add add blank space before and after the sequence  

out.close()#make sure that the last bit of data is physically written to the disk
