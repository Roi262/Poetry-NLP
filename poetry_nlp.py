from constants import *

# TODO
#  1. get all poems
#  2. for each poem, get all lines of the poem
#  3.

class poetry_reader:

    def __init__(self, book_path):
        self.book_path = book_path
        self.file = open(self.book_path)
        self.book_name = ''
        self.author = ''

    def __del__(self):
        self.file.close()

    def get_poems_from_book(self):
        """

        :param book_path: a txt file of a book
        :return: a list of strings - each element is a poem
        """
        lines = self.file.readlines()
        words = []
        for line in lines:
            line = line.replace("{", " ").replace(", ", " ").replace(". ", " ")
            line_words = line.split()
            words += [word.lower() for word in line_words]
        # words_count = count_tokens(words)
        # viz.dict_to_bar_graph(words_count, WORD_COUNT, "4.b GOT")


    def get_all_lines_of_poem(self, poem):
        """

        :param poem: a String of text starting from the title of the poem and ending with the end of the poem.
        :return: a list of all the lines in the poem
        """
        pass



if __name__ == '__main__':
    p_reader_WBlake = poetry_reader(SONGS_OF_INNOCENCE_SONGS_OF_EXPERIENCE_PATH)
    p_reader_WBlake.get_poems_from_book()
    p_reader_WWhitman = poetry_reader(LEAVES_OF_GRASS_PATH)
    p_reader_WWhitman.get_poems_from_book()

