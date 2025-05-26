# AI-Assisted Email Sorting and Response System

This project is a Python-based prototype for automatically classifying incoming emails into predefined themes and sending appropriate auto-responses. It was built for internal use to replace or prototype features similar to a KANA email management system using open-source tools.

---

## 📦 Project Structure
```
email-autoreply/
├── data/
│   └── emails.csv               # Sample or synthetic email dataset
├── models/
│   └── theme_classifier.pkl     # Saved trained model
├── src/
│   ├── preprocess.py            # Text cleaning and preprocessing functions
│   ├── train.py                 # Model training script
│   ├── classify.py              # Email classification script
│   ├── respond.py               # Response generation script
│   ├── integration.py           # Email fetching, classifying, replying script
│   └── generate_synthetic_data.py # Script to generate synthetic training data
```

---

## ⚙ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/email-autoreply.git
cd email-autoreply
```

### 2️⃣ Create and activate the Conda environment
```bash
conda create -n email-proto-py310 python=3.10
conda activate email-proto-py310
```

### 3️⃣ Install dependencies
```bash
conda install numpy pandas scikit-learn nltk spacy transformers email-validator pip
pip install torch imapclient pyzmail36
```

> Note: For Windows + Anaconda, if `pyzmail36` fails, use the updated `integration.py` that relies on `imaplib` + `email` instead (already provided).

### 4️⃣ Prepare the dataset
Generate synthetic data:
```bash
python src/generate_synthetic_data.py
```
This creates a `data/emails.csv` with 100 sample emails.

### 5️⃣ Train the classifier
```bash
python src/train.py
```
This trains a logistic regression classifier and saves the model to `models/theme_classifier.pkl`.

### 6️⃣ Set email credentials (Gmail)
Use a Gmail account with 2FA and an app password.
```bash
set EMAIL_USER=your_email@gmail.com
set EMAIL_PASS=your_16character_apppassword
```

### 7️⃣ Run the integration script (single run)
```bash
python src/integration.py
```
This will:
- Connect to Gmail
- Fetch new (unseen) emails
- Classify them into themes
- Generate template-based replies
- Send replies via SMTP
- Mark emails as seen to avoid repeated processing

---

## 💡 Features
✅ Predefined themes (Billing, Technical Support, Account Changes, General Inquiry)  
✅ Template-based auto-replies  
✅ Logistic regression classifier with TF-IDF features  
✅ Secure credential handling (via environment variables)  
✅ Integration with Gmail IMAP + SMTP  
✅ Synthetic dataset generator for testing

---

## 🚀 Future Improvements
- Switch to a BERT-based classifier for improved accuracy
- Add OAuth2-based Gmail integration (for production use)
- Build a Flask or FastAPI dashboard for monitoring and managing emails
- Log all incoming/outgoing emails to a database or log file
- Add unit tests and CI/CD pipeline

---

## 🔐 Security Notes
- Never hardcode passwords in scripts
- Always use environment variables or `.env` files
- Use a test Gmail account for development
- For production, use OAuth2 (not raw app passwords)

---

## 🙌 Contributors
- **Manoj** — initial prototype, training, and integration

Feel free to fork, extend, and contribute improvements!
