from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        # map each wildcard pattern -> words matching it
        patterns = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                patterns[word[:i] + '*' + word[i+1:]].append(word)

        queue = deque([(beginWord, 1)])   # count includes beginWord
        visited = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                pat = word[:i] + '*' + word[i+1:]
                for nxt in patterns[pat]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))
        return 0