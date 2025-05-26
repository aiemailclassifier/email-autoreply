import joblib

# Load model
model = joblib.load('models/theme_classifier.pkl')

def classify_email(subject, body):
    text = subject + ' ' + body
    return model.predict([text])[0]

### src/respond.py
def generate_reply(theme, sender_name="Customer"):
    templates = {
        "Billing": f"Dear {sender_name},\n\nThank you for your billing inquiry. Our team will review your request and get back to you shortly.\n\nBest,\nSupport Team",
        "Technical Support": f"Dear {sender_name},\n\nThank you for contacting technical support. Please provide more details about your issue so we can assist you better.\n\nRegards,\nSupport Team",
        "Account Changes": f"Dear {sender_name},\n\nYour account change request has been received. We will process it within 2 business days.\n\nBest,\nSupport Team",
        "General Inquiry": f"Dear {sender_name},\n\nThank you for reaching out. We have received your inquiry and will respond soon.\n\nBest,\nSupport Team"
    }
    return templates.get(theme, f"Dear {sender_name},\n\nThank you for your message. We will get back to you shortly.\n\nBest,\nSupport Team")
