from lib.grammar_stats import GrammarStats
import pytest

"""
When we check the garammar of a string by calling check method
Returns a boolean: 
True if starts with capital and ends with suitable punctuation
False otherwise
"""

def test_check_given_bad_grammar():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('hi my name is john') == False

def test_check_given_good_grammar():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('Hi my name is John.') == True

"""
After the object has performed atleast one grammar check
The percentage good function should return an int representing the percentage of checks that returned True
"""

def test_percentage_good():
    grammar_stats = GrammarStats()
    grammar_stats.check('Hi my name is John.')
    grammar_stats.check('hi my name is john')
    grammar_stats.check('Hi my name is John.')
    grammar_stats.check('Hi my name is John.')
    grammar_stats.check('Hi my name is John.')
    assert grammar_stats.percentage_good() == 80

