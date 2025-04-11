import uuid

def generate_ticket():
    return f"TKT-{uuid.uuid4().hex[:6].upper()}"