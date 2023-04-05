"""Knock knock joke with conditionals"""

inter_cow: str = input("Do you want an interrupting cow?")

print("Knock knock")
if (inter_cow == "yes"):
    print("...who's there?")
    print("interrupting cow.")
    print("interrupting cow wh--")
    print("MOO!!")

else:
    print("Oh... okay... :( ")
    if (inter_cow == "you're not funny"):
        print("wow :( you're really mean")
        