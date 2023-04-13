seq ='ATGCAATCGACTACGATCTGAGAGGGCCTAA'#create a string variable seq
#input three stop codons,and count them
a=seq.count('TAG')
b=seq.count('TGA')
c=seq.count('TAA')
d=a+b+c#count the number of stop codons in total
print(d)#print the number of stop codons

