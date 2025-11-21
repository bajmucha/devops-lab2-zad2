# tests/test_app.py

# Prosty test jednostkowy dla funkcji dodaj

from src.app import dodaj


def test_dodaj(): 
    assert dodaj(2, 3) == 6 # zły wynik, test powinien się wyłożyć
