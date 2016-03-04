#bsort, using while to bubble sort a list
def bubble_sort(alist):
	i = 0
	l = len(alist)+1
	while(l > i):
		for b in range(0, l - 2):
			if alist[b] > alist[b+1]:
				alist[b+1] = alist[b]+alist[b+1]
				alist[b] = alist[b+1] - alist[b]
				alist[b+1] = alist[b+1] - alist[b]
				
		i+=1
	
	return alist
