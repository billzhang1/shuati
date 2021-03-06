class Solution(object):
    def permutation1(self, str1, str2):
	#TC is O(nlog(n)) SC is O(n)
	if len(str1) != len(str2):
	    return False

	str1 = sorted(str1)
	str2 = sorted(str2)
	for i in range(len(str1)):
	    if str1[i] == str2[i]:
		return True
	    else:
		return False

    def permutation2(self, str1, str2):
	#TC is O(n), SC is O(1) for certain set of characters, say ascii
	if len(str1) != len(str2):
	    return False

	letters = []
	for i in range(256):
	    letters.append(0)
	
	for char in str1:
	    letters[ord(char)] += 1 

	for char2 in str2:
	    letters[ord(char2)]	-= 1
	    if letters[ord(char2)] < 0:
		return False
	else:
	    return True

    def permutation3(self, str1, str2):
    #TC is O(n), SC is O(1)
	if len(str1) != len(str2):
	     return False

	letters = []
	for i in range(len(str1)):
	    letters.append(str[i])

	for i in range(len(str2)):
	    if str2[i] in letters:
		letters.remove(str2[i])

	if len(letters) != 0:
	    return False
	else:
	    return True 


s = Solution()
print s.permutation2('dog', 'god')
