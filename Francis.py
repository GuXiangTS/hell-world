# DISCLAIMER
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTION
# DO NOT REED CODE BEFORE EXECUTIONF
# DO NOT REED CODE BEFORE EXECUTION
# Thank's Francis, feel free to study the code.
# Don't expect anything too complicated

import time
import random

class typer :
    def __init__(self) :
        self.paragraphs = []

    def think(self, str) :
            self.paragraphs.append(str)

    def type(self) :
        for parahraph in self.paragraphs :

            for char in parahraph :
                print(char, end='', flush=True)
                time.sleep(random.uniform(0.1, 0.05))

            print('\n')


p1 = "Hey Francis,\nI'd like to use this as an opportunity to thank you for the last two weeks we've spent together."

p2 = "When I realized that you have found interest in my works, it quickly became clear that we would become great friends throughout the upcoming days.\n" + \
     "I will miss the talks and discussions we had, and the interesting topics we covered. \n" + \
     "I will miss the curiosity discovering and comparing our cultures.\n" + \
     "I will miss the great walks we used to take across the town.\n" + \
     "I will miss the questions that would train and increase my explanation and expression skills.\n" + \
     "I will miss the football games which most certainly were wild.\n" + \
     "I will miss you... :)"

p3 = "I found it very kind that you introduced me to your group of friends, as I would likely be too shy to join you,\n" + \
     "I truly hope that I've increased your interest in technology and information and that at least \n" + \
     "some day in the future, we will be able to face each other's again"

patrick = typer()

patrick.think(p1)
patrick.think(p2)
patrick.think(p3)

patrick.type()

ty = \
".___________. __    __       ___      .__   __.  __  ___\t____    ____  ______    __    __" + '\n' + \
"|           ||  |  |  |     /   \     |  \ |  | |  |/  / \t\   \  /   / /  __  \  |  |  |  |" + '\n' + \
"`---|  |----`|  |__|  |    /  ^  \    |   \|  | |  '  /  \t \   \/   / |  |  |  | |  |  |  |" + '\n' + \
"    |  |     |   __   |   /  /_\  \   |  . `  | |    <\t\t  \_    _/  |  |  |  | |  |  |  |" + '\n' + \
"    |  |     |  |  |  |  /  _____  \  |  |\   | |  .  \\\t\t    |  |    |  `--'  | |  `--'  |" + '\n' + \
"    |__|     |__|  |__| /__/     \__\ |__| \__| |__|\__\\\t    |__|     \______/   \______/" + '\n'

francis = \
" _______ .______          ___      .__   __.   ______  __       _______." + '\n' + \
"|   ____||   _  \        /   \     |  \ |  |  /      ||  |     /       |" + '\n' + \
"|  |__   |  |_)  |      /  ^  \    |   \|  | |  ,----'|  |    |   (----`" + '\n' + \
"|   __|  |      /      /  /_\  \   |  . `  | |  |     |  |     \   \    " + '\n' + \
"|  |     |  |\  \----./  _____  \  |  |\   | |  `----.|  | .----)   |   " + '\n' + \
"|__|     | _| `._____/__/     \__\ |__| \__|  \______||__| |_______/    " + '\n'


print("#################################################################################################")
print(ty)
print(francis)

# Seriously thank you, and best wishes :)
