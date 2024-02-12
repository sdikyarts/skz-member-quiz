import random

def generate_member(user_choices):

    stray_kids_members = {
        "Bang Chan": {
            "answers": ["Loyal", "Blonde", "Playing Sports", "Pokémon Theme Song", "\"i hate to admit\"", "Pizza", "Wolf"],
            "response": "You got Bang Chan!\nYou're a natural born leader, humble, hardworking, and always know how to make those around you feel safe and comfortable.\nYou love sports, eating pizza with friends, and have great music taste!\nKeep being you and never forget how amazing you are.",
            },
        "Hyunjin": {
            "answers": ["Creative", "Black", "Painting", "\"My My My!\" by Troye Sivan", "\"Charmer\"", "Sushi", "Llama"],
            "response": "You got Hyunjin!\nYou're artistic, kind, and super smart.\nOnce people get to know you, they quickly see just how big your heart is!\nNever stop creating and don't be afraid to chase your many dreams.",
            },
        "Felix": {
            "answers": ["Sweet", "Red", "Shopping", "\"Daylight\" by David Kushner", "\"DOMINO\"", "Rice Cakes", "Koala"],
            "response": "You got Felix!\nYou're sweet like candy and have an amazing fashion sense.\nPeople immediately feel at home around you, and you make people feel seen!\nNever forget how much your energy lifts people up."
            },
        "Seungmin": {
            "answers": ["Calm", "Purple", "Photography", "\"Can't Control Myself\" by TAEYEON", "\"Get Cool\"", "Eggs", "Puppy"],
            "response": "You got Seungmin!\nYou're super talented, have a calming energy, and always know just what to say to lighten the mood.\nYou're someone that your friends can always count on when they need you, but don't forget to also be there for yourself!\nKeep being a ray of sunshine."},
        "I.N": {
            "answers": ["Clumsy", "Pink", "Mukbang Artist", "\"Time of Our Life\" by Day6", "\"Hug Me\"", "Watermelon", "Fox"],
            "response": "You got I.N!\nYou're probably the baby of your friend group, a bit clumsy, and always know the best place to eat.\nYou have a super cute smile, so never stop smiling!"},
        "Han": {
            "answers": ["Funny", "Silver", "Watching Movies", "\"Instagram\" by DEAN", "\"Silent Cry\"", "Cheesecake", "Squirrel"],
            "response": "You got Han!\nYou're super funny and the life of the party.\nWhile you love to have a good time, you also are always down for a chill movie night!\nDon't forget to take some time for yourself and your many hobbies."},
        "Changbin": {
            "answers": ["Cheerful", "Green", "Tattooing", "\"How Do You Sleep?\" by Sam Smith", "\"MIROH\"", "Pasta", "Rabbit"],
            "response": "You got Changbin!\nYou're very cheerful, have unique interests, and are always laughing.\nYou're really just a big teddy bear!\nYour friends love being around you because you can always make them smile."},
        "Lee Know": {
            "answers": ["Unique", "Brown", "Hiking", "\"10 out of 10\" by 2PM", "\"Easy\"", "Jokbal", "Cat"],
            "response": "You got Lee Know!\nYou have a unique personality that people love!\nYou enjoy cooking, being active, and spending time in nature!\nStay focused and driven, and it will get you far."},
    }


    flat_user_choices = [item for sublist in user_choices for item in sublist]

    member_counts = [[member, sum(item in info["answers"] for item in flat_user_choices)] for member, info in stray_kids_members.items()]

    max_count = max(member_counts, key=lambda x: x[1])[1]

    max_members = [item for item in member_counts if item[1] == max_count]

    if len(max_members) > 1:
        selected_member = random.choice(max_members)
    else:
        selected_member = max_members[0]

    return stray_kids_members[selected_member[0]]["response"]


# REFERENCES:
## How can I cheat BuzzFeed: (https://medium.com/@jamiegrove/how-to-cheat-at-buzzfeed-personality-tests-ca81262af3fb)