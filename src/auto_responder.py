def generate_response(category):
    responses = {
        "Login Issue": "Please try resetting your password using the forgot password link.",
        "Payment Issue": "Your payment is being reviewed. You’ll receive an update shortly.",
        "Delivery Issue": "We apologize for the delay. Your package is on the way.",
        "Technical Issue": "Our technical team is actively working on it. Stay tuned!",
        "Account Management": "We are processing your account request. Expect confirmation soon.",
        "Billing Issue": "We’ve flagged the duplicate charge for review. You'll be notified once refunded."
    }
    return responses.get(category, "Thanks for reaching out! We’ll get back to you soon.")