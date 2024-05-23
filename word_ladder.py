"""
Word Ladder
Hard
Topics
Companies

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

 

Constraints:

    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.

"""

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # Initialize queue with the beginWord and set of visited words
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            # Dequeue the word and its level
            word, level = queue.popleft()

            # Iterate over each character in the word
            for i in range(len(word)):
                # Iterate over all possible lowercase letters
                for c in "abcdefghijklmnopqrstuvwxyz":
                    # Skip if the character is the same as in the original word
                    if c == word[i]:
                        continue

                    # Create the new word by replacing the character at index i
                    newWord = word[:i] + c + word[i + 1 :]

                    # Check if the new word is in the wordSet and has not been visited before
                    if newWord in wordSet and newWord not in visited:
                        # Check if the new word is the endWord
                        if newWord == endWord:
                            return level + 1

                        # Enqueue the new word and its level
                        queue.append((newWord, level + 1))

                        # Add the new word to the set of visited words
                        visited.add(newWord)

        # No transformation sequence exists
        return 0
