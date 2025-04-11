import uuid

def generate_ticket(message=None):
    return f"TKT-{uuid.uuid4().hex[:6].upper()}"