class Solution(object):

	def groupAnagrams(self, strs):
		"""
			:type strs: List[str]
			:rtype: List[List[str]]
			"""
		if len(strs) == 1:
			return [strs]
		seen = {}
		for word in strs:
			sorted_word = "".join(sorted(word))
			if sorted_word not in seen:
				seen[sorted_word] = [word]
			else:
				seen[sorted_word].append(word)
		return seen.values()
