import re
f=open('/Users/wd/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')#open the file
count=0#count the number of coding sequences which could be generated using the given stop codon
endcode=input()#encode=the string we typ in
if endcode=='TAA':#if the inpute is 'TAA' 
	out=open('/Users/wd/Desktop/IBI1_2022-23/Practical 9/TAA_stop_genes.fa','w')#open the file TAA_stop_genes.fa and write in.
	separator=''#a parameter used to change list into string
	for line in f:#read the file line by line
		if line.startswith('>'):#recognize line start with" >"
			line1=re.findall(r'^>\S+',line)#find gene name
			name=separator.join(line1)#line1 is a list, we need to change list into string so then out.write()can run
			sequence=''#define sequence
		else:
			line2=line.rstrip()#delete white space at the end of the line
			sequence += line2#add those gene sequence in several lines together
			if sequence.endswith(endcode):#extract the gene end with the encode we typed in
				count=count+1#count the number of gene end with 'encode'
				gene=sequence+'\n'#line feed at the end of the gene
				num1=' '+str(count)+'\n'#compose type
				out.write(name+num1)#write the sequence name
				out.write(gene)#write gene sequence
	out.close()#make sure that the last bit of data is physically written to the disk

if endcode=='TAG':
        out=open('/Users/wd/Desktop/IBI1_2022-23/Practical 9/TAG_stop_genes.fa','w')
        separator=''#a parameter used to change list into string
        for line in f:#read the file line by line
                if line.startswith('>'):#recognize line start with" >"
                        line1=re.findall(r'^>\S+',line)#find gene name
                        name=separator.join(line1)#line1 is a list, we need to change list into string so then out.write()can run
                        sequence=''#define sequence
                else:
                        line2=line.rstrip()#delete white space at the end of the line
                        sequence += line2#add those gene sequence in several lines together
                        if sequence.endswith(endcode):
                                count=count+1
                                gene=sequence+'\n'
                                num1=' '+str(count)+'\n'
                                out.write(name+num1)
                                out.write(gene)
        out.close()#make sure that the last bit of data is physically written to the disk

if endcode=='TGA':
        out=open('/Users/wd/Desktop/IBI1_2022-23/Practical 9/TGA_stop_genes.fa','w')
        separator=''#a parameter used to change list into string
        for line in f:#read the file line by line
                if line.startswith('>'):#recognize line start with" >"
                        line1=re.findall(r'^>\S+',line)#find gene name
                        name=separator.join(line1)#line1 is a list, we need to change list into string so then out.write()can run
                        sequence=''#define sequence
                else:
                        line2=line.rstrip()#delete white space at the end of the line
                        sequence += line2#add those gene sequence in several lines together
                        if sequence.endswith(endcode):
                                count=count+1
                                gene=sequence+'\n'
                                num1=' '+str(count)+'\n'
                                out.write(name+num1)
                                out.write(gene)
        out.close()#make sure that the last bit of data is physically written to the disk
