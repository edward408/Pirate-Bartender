#The Bartender app
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def customer_query(questions):
    """Ask the customers preference """
    responses = {}
    for key, value in questions.iteritems():
        answer = raw_input(value)
        if answer == 'Yes':
            responses[key] = True
        elif answer == 'No':
            responses[key] = False
            
    return responses

responses = customer_query(questions)

def construct_drink(responses):
    """Build the drink with the customers preferred ingredients"""
    drink = []
    for key, value in responses.iteritems():
        if value == True and key in ingredients.iterkeys():
            drink.append(random.choice(ingredients[key]))
            
    return drink
        
if __name__ == '__main__':
    print construct_drink(responses)
