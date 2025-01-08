import random
import requests

# URLs for word lists
ADJECTIVES_URL = 'https://raw.githubusercontent.com/0xstaark/MISC/main/adjectives.txt'
ANIMALS_URL = 'https://raw.githubusercontent.com/0xstaark/MISC/main/animals.txt'

def fetch_word_list(url):
    # Fetch a word list from the provided URL.
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text.split()
    except requests.RequestException:
        print(f"Error: Unable to retrieve words from {url}")
        exit()

def generate_engagement_name(adjectives, animals):
    # Generate a random engagement name using an adjective and an animal.
    return f"{random.choice(adjectives)} {random.choice(animals)}"

def prompt_for_number(prompt, default):
    # Prompt the user for a number with a default value.
    user_input = input(prompt).strip()
    if not user_input:
        return default
    try:
        return int(user_input)
    except ValueError:
        print("Invalid input. Using default.")
        return default

def prompt_for_yes_no(count):
    # Prompt the user for a strict yes or no input.
    while True:
        user_input = input(f"Would you like to generate {count} more names? (Press ENTER to generate, 'n' to exit): ").strip().lower()
        if user_input in ['n', '']:
            return user_input
        print("Invalid input. Please press ENTER to generate or enter 'n' to exit.")

def main():
    # Fetch word lists
    adjectives = fetch_word_list(ADJECTIVES_URL)
    animals = fetch_word_list(ANIMALS_URL)

    # Get the number of names to generate
    default_count = 5
    count = prompt_for_number(f"How many engagement names would you like to generate? (default is {default_count}): ", default_count)

    # Generate and display the requested number of names
    print("\n##########################\nGenerated Engagement Names\n##########################\n")
    for i in range(count):
        print(f"[+] {generate_engagement_name(adjectives, animals)}")
        print()

    # Allow interactive generation of additional names
    while True:
        user_input = prompt_for_yes_no(count)
        if user_input == 'n':
            print("Thank you for using the name generator. Goodbye!")
            break
        else:  # If user presses ENTER
            print("\n##########################\nGenerated Engagement Names\n##########################\n")
            for _ in range(count):
                print(f"[+] {generate_engagement_name(adjectives, animals)}\n")

if __name__ == "__main__":
    main()
