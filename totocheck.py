winner_numbers = '1 18 27 37 44 47'
plus_numbers = '12 15 24 27 31 43'
coupon_path = 'C:\Users\pushpull\Desktop\kupon.txt'

def get_number_list(number_string):
	return number_string.split()

def compare_with_winner_numbers(winner_numbers, compared_numbers):
	compare_with_numbers(winner_numbers, compared_numbers, 'Lotto')

def compare_with_plus_numbers(winner_numbers, compared_numbers):
	compare_with_numbers(winner_numbers, compared_numbers, 'Plus')
	
def compare_with_numbers(winner_numbers, compared_numbers, tototype):
	number_of_hits = 0
	hit_list = []
	for winner_number in winner_numbers:
		for compared_number in compared_numbers[1]:
			if winner_number == compared_number:
				number_of_hits += 1
				hit_list.append(compared_number)
	if 3 <= number_of_hits:
		print 'There are {} hits: {} in {} from {}'.format(number_of_hits, hit_list, compared_numbers[0], tototype)

print winner_numbers
print plus_numbers
f = open(coupon_path,'r')
for line in f:
	line_arr = line.split(':')
	number_line = line_arr[1].split('\n')[0]
	line_tuple = line_arr[0], get_number_list(number_line)
	compare_with_winner_numbers(get_number_list(winner_numbers), line_tuple)
	compare_with_plus_numbers(get_number_list(plus_numbers), line_tuple)
	