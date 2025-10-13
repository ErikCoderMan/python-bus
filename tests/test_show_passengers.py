from show_passengers import ShowPassengers

def test_start_no_passengers(capsys):
    sp = ShowPassengers([])
    sp.Start()
    output = capsys.readouterr().out.strip()
    assert output == "No passengers"

def test_start_with_passengers(capsys):
    passengers = [
        {"name": "Alice", "age": 20, "gender": "Female", "time": "10:00:00"},
        {"name": "Bob", "age": 25, "gender": "Male", "time": "11:00:00"}
    ]
    sp = ShowPassengers(passengers)
    sp.Start()
    lines = capsys.readouterr().out.strip().split("\n")

    assert lines[0] == "Passengers:"
    assert "id: 1" in lines[1] and "Alice" in lines[1]
    assert "id: 2" in lines[2] and "Bob" in lines[2]