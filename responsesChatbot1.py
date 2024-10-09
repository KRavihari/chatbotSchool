import random

R_EATING="I don't like eating anything because I'm bot obviously"
#DRINKING="I don't drink normally as i'm a bot"

def unknown():
    response=['Could you please re-pharse that?',
              "Sorry! I think i am unaware about that",
              "Sounds about right",
              "Can you please google that",
              "What does that mean?"][random.randrange(4)]
    return response