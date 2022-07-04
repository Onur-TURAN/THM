import itertools
 
values = ['England', 'Denmark', 'Nigeria', 'Ukraine', 'Germany']

#generate all permutations with a set of 3
per = itertools.permutations(values, 3)
with open("country.txt", "w") as f:
	for v in per:
		f.write('{}\n'.format(''.join(v)))
		f.close
