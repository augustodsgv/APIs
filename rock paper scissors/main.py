from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/shoot/")
async def shoot(user_weapon : str):
    weapons = ['rock', 'paper', 'scissors']
    if not user_weapon in weapons: return 'Invalid weapon!'
    game_key = {
        ('rock', 'rock'): 'Tie',
        ('rock', 'paper'): 'Lose',
        ('rock', 'scissors'): 'Win',
        ('paper', 'rock'): 'Win',
        ('paper', 'paper'): 'Tie',
        ('paper', 'scissors'): 'Lose',
        ('scissors', 'rock'): 'Lose',
        ('scissors', 'paper'): 'Win',
        ('scissors', 'scissors'): 'Tie',
    }
    computer_weapon = weapons[random.randrange(0, 3)]
    result = game_key[(user_weapon, computer_weapon)]
    return_message = {
        'User_weapon' : user_weapon,
        'Computer_weapon' : computer_weapon,
        'Result' : result
    }
    return return_message
