# devops-lab2-zad2
# DevOps Lab 2 – Task 2

Simple Python project to demonstrate Continuous Integration (CI) using **GitHub Actions** and Discord webhook notifications.

---

## 📦 Includes

- Python program (`src/app.py`)
- Dummy test (`tests/test_app.py`)
- CI workflow (`.github/workflows/ci.yml`)

---

## ⚙️ Requirements

- Python 3.10 / 3.11  
- `pip`  
- `pytest`  
- Linux/macOS/WSL or GitHub Actions runner (`ubuntu-22.04`)

---

## 🚀 Run locally

```bash
git clone https://github.com/bajmucha/devops-lab2-zad2.git
cd devops-lab2-zad2

# install dependencies
pip install -r requirements.txt

# run tests
pytest

# run simple app
python src/app.py
