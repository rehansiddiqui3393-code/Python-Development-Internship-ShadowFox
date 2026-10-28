# Task 2 (Intermediate) - Q2: Hangman with visual progress and hints
import random

STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]

WORDS = {
    "Programming": {
        "python": "A popular language named after a comedy group",
        "variable": "A named place to store a value",
        "function": "A reusable block of code",
        "loop": "Repeats code again and again",
        "dictionary": "Stores key-value pairs",
    },
    "Animals": {
        "elephant": "Largest land animal",
        "giraffe": "Has a very long neck",
        "penguin": "A bird that cannot fly but swims",
        "kangaroo": "Carries its baby in a pouch",
        "tiger": "A big striped cat",
    },
    "Countries": {
        "india": "Home of the Taj Mahal",
        "australia": "Both a country and a continent",
        "japan": "Land of the rising sun",
        "brazil": "Hosts the Amazon rainforest",
        "egypt": "Famous for pyramids",
    },
}

MAX_WRONG = len(STAGES) - 1


def show_word(word, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play():
    print("=" * 40)
    print("        WELCOME TO HANGMAN")
    print("=" * 40)

    category = random.choice(list(WORDS))
    word, hint = random.choice(list(WORDS[category].items()))
    guessed = set()
    wrong = 0
    hint_used = False

    print(f"Category: {category}")
    print("Type a letter to guess, or type 'hint' for a clue (costs 1 life).")

    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        print("\nWord:", show_word(word, guessed))
        print("Guessed letters:", " ".join(sorted(guessed)) or "-")
        print(f"Lives left: {MAX_WRONG - wrong}")

        if all(ch in guessed for ch in word):
            print(f"\nCongratulations! You guessed the word: {word.upper()}")
            return

        choice = input("Your guess: ").strip().lower()

        if choice == "hint":
            if hint_used:
                print("You already used your hint:", hint)
            else:
                hint_used = True
                wrong += 1
                print("HINT:", hint)
            continue

        if len(choice) != 1 or not choice.isalpha():
            print("Please enter a single letter.")
            continue
        if choice in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(choice)
        if choice in word:
            print("Good guess!")
        else:
            wrong += 1
            print("Wrong guess!")

    print(STAGES[MAX_WRONG])
    print(f"\nGame over! The word was: {word.upper()}")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break
