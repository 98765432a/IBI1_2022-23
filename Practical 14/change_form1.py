from xml.dom.minidom import parse
import xml.dom.minidom
import re
import pandas as pd
import numpy as np

DOMTree = xml.dom.minidom.parse("go_obo.xml")#parse the XML file into a DOM document object
collection = DOMTree.documentElement#get the root element of the document
terms= collection.getElementsByTagName("term")#get a list of "term" nodes

#make empty lists
id_out=[]
name_out=[]
defstr_out=[]
child_nodes_out=[]

def child_nodes(ID):
	"""this function is used to count all the childnodes of a gene""" 
	count=0#make definition to count
	for term in terms:
		is_as=term.getElementsByTagName('is_a')#get a list of "is_a" elements
		for is_a in is_as:
			if is_a.firstChild.data==ID:#'the first childnode of the "is_a" node' is equal to the input 'first childnode of the "id" node'
				count+=1
				count+=child_nodes(term.getElementsByTagName('id')[0].firstChild.data)#use the method of iteration add all the childnodes of the gene together
	return count

for term in terms:#for the "term" element in "terms" list

	describe=term.getElementsByTagName('defstr')[0]#get descendants nodelist from 'defstr'
	describe1=describe.childNodes[0].data#the node itself(element in 'defstr' tag).
	if re.search('autophagosome',str(describe1)):#extract all genes about "autophagosome"
		id=term.getElementsByTagName('id')[0]#get a list of "id" nodes and extract the first node
		id1=id.childNodes[0].data#extract the first childnode of the "id" node
		print(id1)
		name=term.getElementsByTagName('name')[0]#get a list of "name" nodes and extract the first node   
		name1=name.childNodes[0].data#get a list of "name" nodes and extract the first node   
		defstr=term.getElementsByTagName('defstr')[0]
		defstr1=defstr.childNodes[0].data
		x=child_nodes(id1)#input parameters to the child_nodes() function

		#add informations about gene to the end of each lists
		id_out.append(id1)
		name_out.append(name1)
		defstr_out.append(defstr1)
		child_nodes_out.append(x)
df=pd.DataFrame({"id":id_out,"name":name_out,"defstr":defstr_out,"child nodes":child_nodes_out})#transform the lists into the form of a DataFrame
df.to_excel('autophagosome.xlsx',index=False)#draw this dataframe into an excel called autophagosome.xlsx
