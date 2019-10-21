import toml

with open("dialogue.txt") as file:
    dialogues = toml.load(file)
print(dialogues['coach'])
