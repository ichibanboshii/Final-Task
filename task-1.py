import random

def generate_password():
    NOUNS = ["dog", "cat", "car", "house", "book", "computer", "tree", "flower", "ocean", "mountain"]
    ADJECTIVES = ["happy", "sad", "big", "small", "fast", "slow", "old", "new", "good", "bad"]
    VERBS = ["run", "walk", "talk", "eat", "drink", "read", "write", "think", "see", "hear"]
    word1 = random.choice(ADJECTIVES)
    word2 = random.choice(NOUNS)
    word3 = random.choice(VERBS)
    password = word1 + word2 + word3
    return password

def main():
    while True:
        try:
            num_passwords = int(input("How many passwords would you like to generate? (1-24):"))
            if 1 <= num_passwords <= 24:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 24.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for i in range(1, num_passwords+1):
        password = generate_password()
        print(f"{i} --> {password}")

if __name__ == "__main__":
    main()
