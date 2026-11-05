
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        max_words = 0

        for sentence in sentences:

            words = sentence.split()

            count = len(words)

            max_words = max(max_words, count)

        return max_words
