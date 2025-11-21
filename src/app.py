# src/app.py

# Prosta funkcja dodawania dwóch liczb
def dodaj(a: int, b: int) -> int:
    return a + b


# Prosty punkt wejścia aplikacji
if __name__ == "__main__":
    wynik = dodaj(2, 3)
    print(f"Wynik dodawania 2 + 3 = {wynik}")
