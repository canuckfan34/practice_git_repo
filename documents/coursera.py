# def  up_to_vowel(s):
# 	''' (str)->str

# 	Return a substring from index 0 to before the first 
# 	vowel found s.

# 	>>>up_to_vowel('hello')
# 	"h"
# 	>>>up_to_vowel("there")
# 	"th"
# 	>>>up_to_vowel("cs")
# 	"cs"
# 	'''

# 	before_vowel=""
# 	i=0

# 	while i < len(s) and not (s[i] in "aeiouAEIOU"):
# 		before_vowel +=s[i]
# 		i +=1
# 	return before_vowel

# up_to_vowel('hello')

# def double_even_indices(lst):
# 	'''(list of int)->NoneType

# 	Double every other int in lst, starting
# 	at index 0.
# 	'''
# 	i=0
# 	while i < len(lst):
# 		lst[i]=lst[i] *2
# 		i +=2
# 	print(lst)

# def secret(s):
# 	i=0
# 	result=''
# 	while s[i].isdigit():
# 		result=result + s[i]
# 		i +=1
# 	return result
# def exampl(L):
# 	i=0
# 	result=[]
# 	while i <len(L):
# 		result.append(L[i])
# 		i= i +3
# 	return result
# def compress_list(L):
# 	'''(Iist of str)-> list of str

# 	Return a new list with adjacent pairs of string elements
# 	in L concatenated together,starting with index 0 and1, then 2 and 3
# 	and so on.

# 	Precondition:len(L) >= 2 and len(L ) % 2 == 0

# 	>>>compress_list(['a','b','c','d'])
# 	['ab','cd']

# 	'''
# 	compressed_list=[]
# 	i=0

# 	while i < len(L):
# 		compressed_list.append(L[i] + L[i + 1])
# 		i=i + 2

# 	return compressed_list

# def sum_list(start,end):
	
# 	total=0
# 	while start <= end:
# 		total=total + start
# 		start=start +2
# 	return total
# def for_sum_list(start,end):
# 	total=0
# 	for i in range(start,end,2):
# 		total=total + i
# 	return total
# def while_version(L):
# 	'''(list of number)-> number

# 	return total sum of all odd numbers, until an even number is found.

# 	>>>while_version([1,3,5,6,7])
# 	9
# 	'''
# 	i=0
# 	total=0

# 	while i < len(L) and L[i] % 2 != 0:
# 		total = total + L[i]
# 		i= i + 1
# 	return total
def print_lol(the_list,level=0):
	''' iterates through all lists, and returns all list
	elements recursively on their own line , also takes
	another argument of level for keeping track of tab stops.'''
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item,level + 1)
		else:
			for tab_stop in range(level):
				print("\t", end=' ')
			print(each_item)
