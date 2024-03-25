from pydantic import BaseModel
from fastapi import FastAPI, Request
import random

app = FastAPI()

# Define endpoints for different game levels and features

class FoodPair(BaseModel):
    food: str
    benefit: str
    side_effect: str

# Sample data for food items and their effects
food_data = [
    {"food": "Spinach", "benefit": "High in iron", "side_effect": "May interfere with blood thinners"},
    {"food": "Salmon", "benefit": "Rich in omega-3 fatty acids", "side_effect": "None"},
    {"food": "Avocado", "benefit": "Contains healthy fats", "side_effect": "High in calories"},
    # Add more food items and effects as needed
]

@app.get("/matching-game")
async def get_matching_game():
    # Shuffle the food data to randomize the order
    random.shuffle(food_data)
    return {"pairs": food_data}

@app.post("/matching-game")
def submit_matching_game_answers(pairs: list[FoodPair]):
    # Check if submitted pairs are correct
    correct_pairs = []
    incorrect_pairs = []

    for pair in pairs:
        for food_item in food_data:
            if pair.food == food_item["food"]:
                if pair.benefit == food_item["benefit"] and pair.side_effect == food_item["side_effect"]:
                    correct_pairs.append(pair)
                else:
                    incorrect_pairs.append(pair)

    # Calculate score or provide feedback
    score = len(correct_pairs)
    feedback = f"You got {score} out of {len(food_data)} correct!"

    return {"score": score, "feedback": feedback, "correct_pairs": correct_pairs, "incorrect_pairs": incorrect_pairs}

@app.get("/puzzle-game")
async def get_puzzle_game():
    # Serve puzzle game interface
    pass

@app.post("/puzzle-game")
async def submit_puzzle_game_solution():
    # Handle submission of puzzle game solution
    pass

# Additional features endpoints

@app.post("/medication-reminder")
async def set_medication_reminder():
    # Set medication reminder
    pass

@app.post("/appointment-scheduling")
async def schedule_appointment():
    # Schedule appointment with healthcare provider
    pass

# Define data models (Pydantic models) for game components

# Define models for Aisha's profile, game levels, puzzles, etc.