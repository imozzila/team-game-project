import toml

with open("dialogue.txt") as file:
    dialogue = toml.load(file)
print(dialogue)
