# Scam Psychological Techniques (PTs) Detection

This project is a web application that analyzes scam messages and identifies the **psychological techniques (PTs)** used to manipulate or deceive victims. Users can input real-life scam texts and receive feedback about the persuasive tactics detected.

---

## What It Does

The app allows users to:
- Enter a scam message in plain text
- Automatically detect and label psychological techniques like **fear**, **urgency**, **authority**, etc.
- Learn how scammers use language to manipulate people

The goal is to raise awareness and help users recognize red flags in scam messages.

---

## Repository Structure
```
scam_website/
├── app.py             # Flask backend that serves the model and website
├── model/
│ ├── pipeline.py      # Script to generate pipeline.pkl (model file)
│ └── pipeline.pkl     # Pre-trained NLP model for PT classification
├── static/            
│ ├── style.css        # CSS Stylesheet
│ ├── index.js          # JavaScript for user interaction
│ ├── search.svg        # Search icon used in the UI
│ └── exclamation-triangle.svg      # Icon for warning display
├── templates/
│ └── index.html        # Main HTML template
├── environment.yml           # Conda environment definition file
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
```
> ⚠ **Note:** The file `pipeline.pkl` is too large to be stored in the GitHub repo.

To generate it yourself:
```bash
cd model
python pipeline.py
```

This will create `pipeline.pkl` and save it in the `model/` directory.

---

## How to Run the Project Locally

> Python 3 is required.

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/scam-website.git
   cd scam-website
   ```

2. **Create and activate the Conda environment:**
   ```bash
   conda env create -f environment.yml
   conda activate scam-pt-env
   ```

   *(If your environment has a different name, replace `scam-pt-env` with whatever is in the `name:` field of your `environment.yml`)*

3. **Generate the machine learning model:**
   ```bash
   cd model
   python pipeline.py
   ```

4. **Run the app:**
   ```bash
   python app.py
   ```

5. **Open in your browser:**
   ```
   http://127.0.0.1:5000/
   ```
---

## Contributors

- **Allie Britton**  
- **Aryan Patel**  
- **Mentor:** Shang Ma

---
