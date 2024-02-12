from answers import *

def ask_questions():
    questions = [
        "First, how would your friends describe you?",
        "Next, which hair color suits your bias most?",
        "Choose a hobby for your day off!",
        "Next, choose a song to play on repeat!",
        "Now, choose a Stray Kids song that fits you best!",
        "Pick something tasty to eat!",
        "Lastly, pick an animal that describes you!"
    ]

    choices = [
        ["Loyal", "Unique", "Creative", "Sweet", "Calm", "Clumsy", "Funny", "Cheerful"],
        ["Red", "Purple", "Black", "Brown", "Blonde", "Green", "Pink", "Silver"],
        ["Playing Sports", "Painting", "Tattooing", "Watching Movies", "Shopping",
        "Photography", "Mukbang Artist", "Hiking"],
        ["\"10 out of 10\" by 2PM", "\"How Do You Sleep?\" by Sam Smith", 
        "\"Daylight\" by David Kushner", "\"My My My!\" by Troye Sivan", 
        "\"Can't Control Myself\" by TAEYEON", "\"Time of Our Life\" by Day6", 
        "\"Instagram\" by DEAN", "Pokémon Theme Song"],
        ["\"MIROH\"", "\"Charmer\"", "\"Silent Cry\"", "\"Get Cool\"", "\"DOMINO\"", "\"Hug Me\"", 
        "\"Easy\"", "\"i hate to admit\""],
        ["Sushi", "Pizza", "Rice Cakes", "Eggs", "Watermelon", "Cheesecake", "Pasta", "Jokbal"],
        ["Wolf", "Llama", "Koala", "Puppy", "Fox", "Squirrel", "Rabbit", "Cat"],
    ]

    responses = []

    for i in range(len(questions)):
        print(questions[i])
        for j in range(len(choices[i])):
            print(f"{j+1}. {choices[i][j]}")
        user_answer = input("Please enter the number of your choice: ")
        responses.append([int(user_answer)])
        print("\n")

    responses = [[response[0] - 1] for response in responses]

    converted_responses = [[choices[i][response[0]]] for i, response in enumerate(responses)]

    member = generate_member(converted_responses)

    return member

