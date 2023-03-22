"""Exercise 6: Choose your own adventure."""
"""Choose your own adventure: growing a plant."""

__author__ = "730314385"

points: int = 0
player: str = ""
plant_emoji: str = "\U0001f331"
sunflower_emoji: str = "\U0001F33B"
tulip_emoji: str = "\U0001F337"
rose_emoji: str = "\U0001F339"
skull_emoji: str = "\U00002620"
water_emoji: str = "\U0001F4A7"
butterfly_emoji: str = "\U0001F98B"
sun_emoji: str = "\U00002600"
flower: str = ""


def greet() -> None: 
    """Welcome message and greeting."""
    print("Welcome to Kaitlin's Fields! Here you can plant  with me or look around if you want!")
    player: str = input("What is your name?: ")
    print(f"That's a great name, {player}!")
    planting: str = input("Would you like to plant something or just look around? Type 'plant' or 'look around': ")
    if planting == "plant":
        garden: str = input("That's great! What kind of flower would you like to plant? A 'sunflower', 'tulip', or 'rose'?: ")
        if garden == "sunflower" or "tulip" or "rose":
            plant(garden)  
        elif garden != "sunflower" or "tulip" or "rose":
            print("Sorry, that wasn't one of the options.")
    elif planting == "look around":
        loser()


def loser() -> None:
    """That's okay! Have a look around."""
    print("That's okay. Have a look around!")
    print(sunflower_emoji + tulip_emoji + butterfly_emoji + rose_emoji + butterfly_emoji + tulip_emoji + sunflower_emoji)


def plant(flower_type: str) -> None:
    """What flower would you like in your garden?"""
    global flower
    print(f"Oh, I LOVE {flower_type}s. Great choice!")
    print(f"Okay then, let's plant a {flower_type}. {plant_emoji}")
    if flower_type == "sunflower":
        flower = sunflower_emoji
    elif flower_type == "tulip":
        flower = tulip_emoji
    elif flower_type == "rose":
        flower = rose_emoji
    watering(flower_type)


def watering(flower_type: str) -> None:
    """Should we water our garden?"""
    global flower
    water: str = input("Do you want to water our plant? 'yes' or 'no': ")
    if water == "yes":
        print(f"Great! {flower_type}s need lots of water to grow.")
    elif water == "no":
        print("Okay! Let's move on then.")
        flower = skull_emoji
    sunshine(flower_type)


def sunshine(flower_type: str) -> None:
    """Is there enough sunshine for our garden?""" 
    global flower
    from random import choice
    sun: str = input("Do you think our plant has enough sunlight? 'yes', 'no', 'i'm not sure, can you tell me?': ")
    if sun == "i'm not sure, can you tell me?":
        sun = choice(['yes', 'no'])
        print(f'Does it have enough sun? It looks like {sun}!')
    if sun == "yes":
        print(f'Woohoo! {flower_type}s need alot of sun to grow big and strong.')
    elif sun == "no":
        flower = skull_emoji
        print("Okay! Next step!")
    results(flower_type)


def results(flower_type: str) -> None:
    """Are you ready for the big reveal of your new plant?"""
    global flower
    ready: str = input("Do you want to see your new plant? 'yes' or 'no': ")
    if ready == "yes":
        if flower == skull_emoji:
            print(flower)
            print("Oh no, something went wrong! Our plant must have not gotten enough water or sun and died. Try again next time!")
        else:
            print(flower)
            print(f"Look at that beautiful {flower_type}! You did a great job.")
            print("Stop by again later if you want to plant something else or have a look around! Bye! ")
    elif ready == "no":
        print("Okay I guess! You can always stop by again to plant something different. See you later!")


def main() -> None:
    """Checks to see if playing."""
    playing: str = input("Would you like to play? type: 'yes' or 'no': ")
    if playing == "yes":
        greet()
    else:
        print("That's alright. I'll see you around!")
    """Would you like to plant a garden with me or just have a look around?"""


if __name__ == "__main__":
    main()