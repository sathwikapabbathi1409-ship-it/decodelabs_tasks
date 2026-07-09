# 🎓 Student Pass/Fail Prediction — Data Classification Using AI

> **DecodeLabs Industrial Training Kit — Project 2 — Batch 2026**

A beginner-friendly supervised learning project that predicts whether a
student **passes or fails** based on hours studied, attendance percentage,
and assignments completed — using Logistic Regression.

## 📌 Overview

| Stage | What happens |
|---|---|
| **Input** | Load `data/student_data.csv`, scale the features |
| **Process** | Train/test split (80/20), train a Logistic Regression classifier |
| **Output** | Accuracy, F1 Score, Confusion Matrix (printed + saved as PNG) |

## 📂 Project Structure

```
.
├── data/
│   └── student_data.csv       # 60-row dataset
├── src/
│   └── classify.py            # main script
├── output/
│   └── confusion_matrix.png   # generated after running
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the project
```bash
python src/classify.py
```

## ✅ Expected Output

The script prints four labeled stages: dataset overview, train/test split
sizes, model training confirmation, and evaluation metrics (accuracy ~90%,
F1 score, classification report, confusion matrix). It saves a chart to
`output/confusion_matrix.png` and finishes by predicting one new,
made-up student.

## 🛠 Troubleshooting

| Error | Fix |
|---|---|
| `ModuleNotFoundError` | Activate your venv, then re-run `pip install -r requirements.txt` |
| `FileNotFoundError: data/student_data.csv` | Run the script from the repo root, not from inside `src/` |
| No plot window appears | Expected — the script saves the plot to a file instead. Open `output/confusion_matrix.png` |

## 🔮 Ideas to Extend

- Swap `LogisticRegression` for `DecisionTreeClassifier` or `KNeighborsClassifier` and compare accuracy
- Change `test_size` in `src/classify.py` and observe the effect
- Add new feature columns to the dataset and retrain
- Batch-predict multiple new students instead of one

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
