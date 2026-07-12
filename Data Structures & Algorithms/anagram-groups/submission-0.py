class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort the strings
        # if the sorted string is in the hashmap, append the unsorted string 
        # to the value 

        sortedToUnsortedWords = defaultdict(list)

        for i in range(len(strs)):
            sortedWord = sorted(strs[i])
            sortedToUnsortedWords[str(sortedWord)].append(strs[i])

        return sortedToUnsortedWords.values()