import pytest
from remove_passenger import RemovePassenger
from unittest.mock import patch
from datetime import datetime

# Helper function to create a passenger dictionary
def make_passenger(name, age, gender, time=None):
    if time is None:
        time = datetime.now().strftime("%H:%M:%S")
        
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "time": time
    }

def test_remove_valid_index():
    passengers = [
        make_passenger("Alice", 25, "female"),
        make_passenger("Bob", 30, "male"),
        make_passenger("Charlie", 22, "male")
    ]
    remover = RemovePassenger(passengers)

    with patch("builtins.input", return_value="1"):
        remover.Start()

    # Bob should be removed from the list
    assert len(passengers) == 2
    assert passengers[0]["name"] == "Alice"
    assert passengers[1]["name"] == "Charlie"

def test_remove_invalid_index():
    passengers = [
        make_passenger("Alice", 25, "female"),
        make_passenger("Bob", 30, "male")
    ]
    remover = RemovePassenger(passengers)

    with patch("builtins.input", return_value="5"):
        remover.Start()

    # No passenger should be removed since index is out of range
    assert len(passengers) == 2
    assert passengers[0]["name"] == "Alice"
    assert passengers[1]["name"] == "Bob"

def test_remove_non_numeric_input():
    passengers = [
        make_passenger("Alice", 25, "female"),
        make_passenger("Bob", 30, "male")
    ]
    remover = RemovePassenger(passengers)

    with patch("builtins.input", return_value="abc"):
        remover.Start()

    # No passenger should be removed since input is not numeric
    assert len(passengers) == 2
    assert passengers[0]["name"] == "Alice"
    assert passengers[1]["name"] == "Bob"

def test_remove_first_and_last():
    passengers = [
        make_passenger("Alice", 25, "female"),
        make_passenger("Bob", 30, "male"),
        make_passenger("Charlie", 22, "male")
    ]
    remover = RemovePassenger(passengers)

    # Remove the first passenger
    with patch("builtins.input", return_value="0"):
        remover.Start()
        
    assert passengers[0]["name"] == "Bob"

    # Remove the last passenger (now index 1)
    with patch("builtins.input", return_value="1"):
        remover.Start()
        
    assert passengers[0]["name"] == "Bob"
    assert len(passengers) == 1

def test_remove_from_empty_list():
    passengers = []
    remover = RemovePassenger(passengers)

    with patch("builtins.input", return_value="0"):
        remover.Start()

    # The list should remain empty
    assert passengers == []
