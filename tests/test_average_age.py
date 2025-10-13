import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from average_age import AverageAge


#Test1: Controls if passenger list is empty
def test_average_age_no_passengers():
    passengers = []
    avg = AverageAge(passengers)
    result = avg.Start()
    assert result == "No passengers are on the bus."


# Test2: If passenger missing age key
def test_average_age_missing_age_key():
    passengers = [
        {"name": "David"},
        {"name": "Erik", "age": 29},
        {"name": "Gabriella", "age": 29}
    ]
    avg = AverageAge(passengers)
    result = avg.Start()
    assert result == "Average age of passengers is: 29.0 years"


# Test3: If all passengers missing age
def test_all_ages_missing():
    passengers = [
        {"name": "David"},
        {"name": "Erik"},
        {"name": "Gabriella"}
    ]
    avg = AverageAge(passengers)
    result = avg.Start()
    assert result == "No ages available for passengers."


# Test4: Controls normal case
def test_average_age_normal_case():
    passengers = [
        {"name": "David", "age": 33},
        {"name": "Gabriella", "age": 29},
        {"name": "Erik", "age": 29}
    ]
    avg = AverageAge(passengers)
    result = avg.Start()
    assert result == "Average age of passengers is: 30.3 years"