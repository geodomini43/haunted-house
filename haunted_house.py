#!/usr/bin/env python3
import random, sys, time

WELCOME = r"""
   .-.      .-.      .-.      .-.      .-.      .-.   
  (   )    (   )    (   )    (   )    (   )    (   )
   '-'      '-'      '-'      '-'      '-'      '-'
   ___   ___   ___   ___   ___   ___   ___   ___
  /___\ /___\ /___\ /___\ /___\ /___\ /___\ /___\
"""

SCENARIOS = [
    ("a creaky attic", "You find a dusty old diary. Inside is a recipe for pumpkin soup—yum!"),
    ("the basement", "A ghost appears! It asks for a joke. You tell a pun and it vanishes."),
    ("the kitchen", "A witch is stirring a cauldron. She offers you a sip of ‘code‑brew’."),
    ("the garden", "Jack‑O‑lanterns light the path. One winks at you and rolls away."),
    ("the hallway", "A portrait follows you with its eyes. You politely ask it to stop staring."),
]

def slow_print(txt, delay=0.04):
    for ch in txt:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    slow_print(WELCOME, 0.02)
    slow_print("\nWelcome to the Haunted House, brave coder!\n")
    name = input("Enter your spooky alias: ").strip() or "Anonymous"
    slow_print(f"\nAlright, {name}… let's explore...")

    location, outcome = random.choice(SCENARIOS)
    slow_print(f"\nYou creep down into {location}...")
    time.sleep(1.5)
    slow_print(outcome)

    score = random.randint(0, 100)
    slow_print(f"\nYour spook‑score: {score}/100")
    if score > 70:
        slow_print("You're practically a Halloween legend! 🏆")
    else:
        slow_print("Better luck next time—keep coding those spells!")

    slow_print("\nThanks for playing. May your bugs be few and your pumpkins many!")
    sys.exit(0)

if __name__ == "__main__":
    main()