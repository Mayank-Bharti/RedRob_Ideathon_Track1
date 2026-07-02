# backend/memory.py
memory = {
    "age": None,
    "income": None,
    "occupation": None,
    "expected_field": None  # new
}

def update_memory(key, value):
    """Update memory, handle contradictions"""
    if key in memory and memory[key] != value:
        # If contradictory info, ask for confirmation
        print(f"Warning: {key} changed from {memory[key]} to {value}")
    memory[key] = value

def get_memory():
    return memory

def clear_memory():
    memory.clear()
