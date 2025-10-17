class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.unread_chunk = []

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f'{self.title}: {self.contents}'

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        text = self.format()
        text_tuple = text.split()
        return len(text_tuple)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        num_words = self.count_words()
        time_to_read = num_words / wpm
        return time_to_read

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.

        if len(self.unread_chunk) == 0:
            text = self.format()
            text_list = text.split()
            self.unread_chunk = text_list


        words_per_chunk = int(wpm * minutes)

        chunk = self.unread_chunk[:words_per_chunk]

        chunk_string = ' '.join(chunk)

        del self.unread_chunk[:words_per_chunk]

        return chunk_string

        
        
