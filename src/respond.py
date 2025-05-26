def generate_reply(theme, sender_name="Customer"):
    templates = {
        "Billing": f"Dear {sender_name},\n\nThank you for your billing inquiry. Our billing team has received your request and will get back to you within 1-2 business days. If you have any supporting documents or references, please attach them to help us process your request faster.\n\nBest regards,\nSupport Team",

        "Technical Support": f"Dear {sender_name},\n\nThank you for reaching out to technical support. Could you please provide more details about the issue you’re facing (such as screenshots, error messages, or steps to reproduce)? This will help our team assist you more efficiently.\n\nRegards,\nTechnical Support Team",

        "Account Changes": f"Dear {sender_name},\n\nWe have received your request for account changes. Please allow 1-2 business days for processing. If you have any urgent requirements or additional instructions, kindly let us know.\n\nBest,\nAccount Management Team",

        "General Inquiry": f"Dear {sender_name},\n\nThank you for your message. We appreciate you contacting us and will review your inquiry shortly. One of our team members will follow up with you as soon as possible.\n\nBest regards,\nCustomer Service Team"
    }

    # Default fallback response if theme is unknown
    default_reply = f"Dear {sender_name},\n\nThank you for your message. We have received your email and will get back to you shortly.\n\nBest,\nSupport Team"

    return templates.get(theme, default_reply)
