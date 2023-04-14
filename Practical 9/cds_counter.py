import re
seq ='ATGCAATCGACTACGATCTGAGAGGGCCTAA'#import the sequence
subseq=re.findall(r'ATG.+',seq)#extract the sequence start from ATG
sub_seq=str(subseq)#change subseq into string
a=re.findall(r'TGA|TAA|TAG',sub_seq)#find the number of TGA|TAA|TAG in sub_seq
num=len(a)#count the number of stop codons
print(num)
