import datetime
from unittest.mock import patch
from add_passenger import AddPassenger

def test_add_passenger(monkeypatch):
    passengers = []
    inputs = iter(["Asad", "23", "Male"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    fake_time = datetime.datetime(2025, 1, 1, 12, 0, 0)

    with patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = fake_time
        mock_datetime.strftime = datetime.datetime.strftime
        add = AddPassenger(passengers)
        add.start()

    assert len(passengers) == 1
    p = passengers[0]
    assert p["name"] == "Asad"
    assert p["age"] == 23
    assert p["gender"] == "Male"
    assert p["time"] == "12:00:00"




