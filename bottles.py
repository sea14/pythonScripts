REFRAIN = '''
%d bottles of pop on the wall,
%d bottles of pop on the wall,
take one down, pass it around,
%d bottles of pop on the wall!
'''

LAST_REFRAIN = '''
%d bottle of pop on the wall,
%d bottle of pop on the wall,
take it down, pass it around,
no more bottles of pop on the wall!
'''

bottles_of_pop = 99
while bottles_of_pop > 1:
	
	print REFRAIN % (bottles_of_pop, bottles_of_pop,
		bottles_of_pop - 1)

	bottles_of_pop -= 1
