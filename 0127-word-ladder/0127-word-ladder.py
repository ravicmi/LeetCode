class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alp = 'qwertyuiopasdfghjklzxcvbnm'
        alp = [a for a in alp]
        if endWord not in wordList: 
            return 0 
        neigh = dict()
        min_path_dict = dict()
        wordList = set(wordList)
        wordList.add(beginWord)
        for word in wordList:
            wordneigh = set()
            for i in range(len(word)):
                new_word = word
                for a in alp:
                    new_word = word[:i] +a +word[i+1:]
                    if new_word in wordList and new_word != word:
                        wordneigh.add(new_word)
            neigh[word] = wordneigh
        # global global_min
        # global_max = 0 
        print(neigh)
        visited = set()
        visited.add(endWord)
        distance = 1
        neigh_level = {endWord}
        found = 0 
        while neigh_level: 
            temp = []
            if beginWord in neigh_level:
                found = 1
                break
            for nei in neigh_level:
                nei_neigh = neigh[nei]
                for w in nei_neigh:
                    if w not in visited:
                        temp.append(w)
                        visited.add(w)
                
            distance +=1 
            neigh_level = temp
        return distance if found else 0

