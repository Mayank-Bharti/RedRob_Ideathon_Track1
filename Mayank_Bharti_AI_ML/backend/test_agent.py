from agent import agent_step
from memory import memory, update_memory

# Clear memory for fresh test
memory.clear()

print("=== AGENT TEST ===")

while True:
    user_input = input("User (Hindi text): ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = agent_step(user_input)
    print("Agent:", response)
