import re
f=open('/Users/wd/Downloads/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')#open the file
endcode=input('please enter TAA/TAG/TGA:')#encode=the string we typ in
output=f"{endcode}_stop_genes.fa"#put the input into the file name
out=open(output,'w')#open the file TAA/TAG/TGA_stop_genes.fa and write in.
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
                                num_endcode=re.findall(endcode,sequence)
                                count=len(num_endcode)#count the number of gene end with 'encode'
                                gene=sequence+'\n'#line feed at the end of the gene
                                num1=' '+str(count)+'\n'#compose type
                                out.write(name+num1)#write the sequence name
                                out.write(gene)#write gene sequence
out.close()#make sure that the last bit of data is physically written to the disk
