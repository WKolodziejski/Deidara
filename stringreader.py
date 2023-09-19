class StringReader:
    i: int
    word: str

    def __init__(self, word: str):
        self.word = word
        self.i = 0

    def read(self, c: int):
        char = self.word[self.i: self.i + c]
        self.i += c

        if char:
            return char

        return None
