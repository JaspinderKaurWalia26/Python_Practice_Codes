# Fake Headline Generator 
import random
subjects = ["Shah Rukh Khan",
            "Virat Kohli",
            "Normala Sitaraman",
            "A Mumbai cat",
            "A group of monkeys",
            "Prime minister modi",
            "Auto Rikshaw from Delhi"
            ]

actions = [
    "launches",
    "cancels",
    "eats",
    "dances with",
    "Declare war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai local train",
    "a plate of samosa",
    "during IPL match",
    "at Ganga Ghat",
    "at India Gate",
    "inside Parliament"
]

def news_generator(list1,list2,list3):
    first_part=random.choice(list1)
    second_part=random.choice(list2)
    third_part=random.choice(list3)
    news=first_part +" "+second_part +" "+ third_part
    return news
new=news_generator(subjects,actions,places_or_things)
print(new)
    
