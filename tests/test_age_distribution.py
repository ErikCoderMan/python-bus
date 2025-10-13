import pytest
from age_distribution import AgeDistribution
import matplotlib.pyplot as plt
from unittest.mock import patch

def test_empty_passengers(monkeypatch):
    ad = AgeDistribution([])
    # Mock plt.show so no plot window appears
    with patch.object(plt, 'show'):
        ad.show_age_distribution()  # should not raise any errors

def test_age_distribution_histogram(monkeypatch):
    passengers = [
        {"name": "Alice", "age": 25, "gender": "Female", "time": "12:00:00"},
        {"name": "Bob", "age": 35, "gender": "Male", "time": "12:05:00"},
        {"name": "Charlie", "age": 45, "gender": "Male", "time": "12:10:00"},
    ]
    ad = AgeDistribution(passengers)
    
    with patch.object(plt, 'show') as mock_show:
        ad.show_age_distribution()
        # Check that plt.show was actually called
        mock_show.assert_called_once()

def test_age_distribution_only_ages(monkeypatch):
    # Test that only passengers with 'age' are included
    passengers = [
        {"name": "Alice", "age": 25},
        {"name": "Bob"},  # missing age
        {"name": "Charlie", "age": 45},
    ]
    ad = AgeDistribution(passengers)
    with patch.object(plt, 'show'):
        ad.show_age_distribution()  # should execute without errors
