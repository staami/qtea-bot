
from random import (choice, randint)

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return "Well, you're awfully silent..."
    elif "hello" in lowered:
        return "Hello there, qt!"
    elif "how are you" in lowered:
        return "I'm great, thanks for asking!"
    elif "bye" in lowered:
        return "Catch 'ya later!"
    elif "roll dice" in lowered:
        return f"You rolled a {randint(1, 6)}!"
    else:
        return choice(["I'm not quite sure that I understand...", "What are you on about?", "Can you rephrase that for me?"])

