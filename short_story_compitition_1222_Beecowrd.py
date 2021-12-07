""" '15% wrong ans' from Beecrawd compiler but I didn't find the fault! Help me if you can.."""
def myMethod(lineNo,CharNo,stories):
	""" just calculate the required pages for publish the stories and return num of pages"""
	pages =[]
	i = 0
	while i<len(stories):
		storyLen = len(stories[i])
		
		LineReq = int(storyLen/CharNo[i])
		if storyLen%CharNo[i] != 0:
			LineReq+=1
			
		PageReq = int(LineReq/lineNo[i])
		if LineReq%lineNo[i] != 0:
			PageReq+=1
			
		pages.append(PageReq)
		i+=1
	return pages

	
wordNo=[] 
lineNo=[] 
CharNo = []
stories =[]

while True:
	""" Getting input till EOF or Value Error Occure """
	try:
		""" variable n contains number of maximum word in story,
		varible l contains number of max line in a page and 
		c contains maximum Char in a line  """
		n, l, c = map(int,input().split())
		wordNo.append(n)
		lineNo.append(l)
		CharNo.append(c)

		""" Getting the story from users. If the story contains
		more word than indicates before(story > n words) then we
		have to cut the long part of it. """
		
		story = str(input())
		spaceCount = story.count(' ')
		if spaceCount == n-1:         # In case story is okay.Though the number of white space is less one than words
			stories.append(story)
		else:                         # In case the story is longer!
			""" Finding the position of white space and concatenate the words and space
			with the help of white space position. But ignore space before last word """
			temp = ''
			k = 0 
			for m in range(n):
				position = story.find(' ',k)
				temp = temp + story[k:position]
				if n-m>=2:
					temp = temp+' '

				k= position+1
			stories.append(temp)
	except (EOFError,ValueError):
		break

get = myMethod(lineNo,CharNo,stories)

print(stories)
for j in range(len(get)):
	print(get[j])

""" Input:
14 4 20
Se mana Piedade tem casado com Quincas Borba apenas me daria uma esperanca colateral
16 3 30
No dia seguinte entrou a dizer de mim nomes feios e acabou alcunhando me Dom Casmurro
5 2 2
a de i de o
5 2 2
a e i o u
    Output:
2
1
3
3
"""