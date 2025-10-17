from lib.diary_entry import DiaryEntry

"""
When a diary entry is created with a title and contents
The title and contents are reflected in their corresponding attributes
"""

def test_create_diary_entry():
    diary_entry = DiaryEntry('First Day of School', 'School was long and boring')
    assert diary_entry.title == 'First Day of School'
    assert diary_entry.contents == 'School was long and boring'


"""
When a diary entry is created with a title and contents
And we format the diary entry
It returns a string with the title and contents
"""

def test_format_diary_entry():
    diary_entry = DiaryEntry('First Day of School', 'School was long and boring')
    assert diary_entry.format() == 'First Day of School: School was long and boring'

"""
Given a diary entry
Returns the number of words in the diary entry
"""

def test_count_num_of_words():
    diary_entry = DiaryEntry('First Day of School', 'School was long and boring')
    assert diary_entry.count_words() == 9

"""
Given a speed to read the contents at
Returns the time it will take to read the contents in seconds
"""

def test_estimate_reading_time():
    diary_entry = DiaryEntry('First Day of School', 'School was long and boring')
    assert diary_entry.reading_time(200) == 9 /200

"""
Given the speed at which the user can read and the amount of time the user has to read
Return a string: the chunk of text the user will be able to read in that time
"""

def test_reading_chunk():
    diary_entry = DiaryEntry('First Day of School', 'School was long and boring')
    assert diary_entry.reading_chunk(1, 5) == 'First Day of School: School'
    assert diary_entry.reading_chunk(1, 5) == 'was long and boring'