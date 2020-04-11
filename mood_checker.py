mood = input("What is your mood today? ").lower().strip()

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Don't be sad. Let's go for a beer instead!")
elif mood == "excited":
    print("Great! What are you excited about?")
elif mood == "relaxed":
    print("Good. Are you practicing meditation?")
else:
    print("I don't recognize this mood.")