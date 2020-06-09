class Solution:
	def romanToInt(self, s: str) -> int:
		ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

		sum = 0
		digit = []
		for roman in s:
			digit.append(ref[roman])

		digit.reverse()

		i = 0
		while (True):
			if i<len(digit)-1:
				if (digit[i] > digit[i + 1]):
					sum = sum + digit[i] - digit[i + 1]
					i = i + 2
					continue
				else:
					sum += digit[i]
					i = i + 1
			else:
				if(i==len(digit)-1):
					return sum + digit[i]
				else:
					return sum



if __name__ == "__main__":
	func = Solution()
	number = func.romanToInt('IV')
	print(number)
	number = func.romanToInt('III')
	print(number)
	number = func.romanToInt('MCMXCIV')
	print(number)
	number = func.romanToInt('LVIII')
	print(number)

dictionary = {1: '(', 2: ')', 3: '{', 4: '}', 5: '[', 6: ']', 7: '', 8: ''}

i = 1

bracket_type = {}

# first find if the pair exist
bracket_type['('] = [];
for i, string in enumerate(s):
	if (s == '('):
		bracket_type['('].append(i)

	if (s == ')'):
		bracket_type[')'].append(i)

	if (s == '{'):
		bracket_type['{}'].append(i)

	if (s == '}'):
		bracket_type['}'].append(i)

	if (s == '['):
		bracket_type['['].append(i)

	if (s == ']'):
		bracket_type[']'].append(i)

for i in range(len(bracket_type) - 1):
	for start_index in bracket_type[i]:
		for end_index in bracket_type[i + 1]:
			if (start_index % 2 == 0 and end_index % 2 == 1 and end_index > start_index):
				result = True
			elseif(start_index % 2 == 1 and end_index % 2 == 0 and end_index > start_index)
			result = True




