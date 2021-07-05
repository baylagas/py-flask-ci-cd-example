from app import home


def test_index():
    assert home() == "this is my main site"
