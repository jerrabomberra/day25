PLACEHOLDER = "[name]"


with open("input/Letters/starting_letter.txt", "r") as file:
    letter = file.read()

with open("input/Names/invited_names.txt", "r") as file:
    invites = file.readlines()
    for name in invites:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(
            f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w"
        ) as completed_letter:
            completed_letter.write(new_letter)
