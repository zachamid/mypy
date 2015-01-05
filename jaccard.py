#!/usr/bin/python

def levenshteinDistance(str1,str2,len1,len2):
	if len1 == 0:
		return len2
	if len2 == 0:
		return len1
	
	cost = 1
	if str1[len1-1]==str2[len2-1]:
		cost = 0
	
	return min(levenshteinDistance(str1,str2,len1-1,len2)+1,
	levenshteinDistance(str1,str2,len1,len2-1)+1,
	levenshteinDistance(str1,str2,len1-1,len2-1)+cost)

def levenshteinIndex(str1,str2):
	distance = levenshteinDistance(str1,str2,len(str1),len(str2))
	return 1-(float)(distance)/max([len(str1),len(str2)])
	
def jaccard(dict1, dict2):
	intersection = 0
	if type(dict1)==dict and type(dict2)==dict:
		for field in dict1:
			if field in dict2:
				if type(dict1[field])==str and type(dict2[field])==str:
					intersection += levenshteinIndex(dict1[field],dict2[field])
				if (type(dict1[field])==int and type(dict2[field])==int) or (type(dict1[field])==float and type(dict2[field])==float) or (type(dict1[field])==long and type(dict2[field])==long):
					intersection += 1-abs((float)(dict1[field] - dict2[field]))/max([dict1[field],dict2[field]])
				if (type(dict1[field])==dict and type(dict2[field])==dict) or (type(dict1[field])==list and type(dict2[field])==list):
					intesection += jaccard(dict1[field],dict2[field])
	else:
		for x in xrange(0,min([len(dict1),len(dict2)])):
			if type(dict1[x])==str and type(dict2[x])==str:
				intersection += levenshteinIndex(dict1[x],dict2[x])
			if (type(dict1[x])==int and type(dict2[x])==int) or (type(dict1[x])==float and type(dict2[x])==float) or (type(dict1[x])==long and type(dict2[x])==long):
				intersection += 1-abs((float)(dict1[x] - dict2[x]))/max([dict1[x],dict2[x]])
			if (type(dict1[x])==dict and type(dict2[x])==dict) or (type(dict1[x])==list and type(dict2[x])==list):
				intesection += jaccard(dict1[x],dict2[x])
	union = len(dict1)+len(dict2)-intersection
	return intersection/union


dict1 = ['name', [1,1,2,3,'hello'],'age',1]
for i in xrange(0,100):
	dict2 = ['name',[1,2,2,3,'Hello'] ,'age',i]
	print jaccard(dict1,dict2)