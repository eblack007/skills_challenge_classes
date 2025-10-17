class GrammarStats:
    def __init__(self):
        self.good_counter = 0
        self.counter = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        ending_punctuation = ['!', '.', '?']
        if text[0].isupper() and text[-1] in ending_punctuation:
            self.good_counter += 1
            self.counter += 1
            return True
        self.counter += 1
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return int((self.good_counter / self.counter) * 100)
