import random
import json
from dataclasses import dataclass

ARM_WRESTLE = "arm wrestle"
DANCE_OFF = "dance off"
RACE = "race"

PLAYER_WON = "player won"
PLAYER_LOST = "player lost"
TIE = "tie"

def random_battle_type():
  # Returns a randomly chosen battle type
  return random.choice([ARM_WRESTLE, DANCE_OFF, RACE])

def select_monatures(monatures, party_size, random_select):
  selected_monatures = []
  if random_select:
    # Choose the monatures randomly
    selected_monatures = random.sample(monatures, party_size)
  else:
    # Choose the first monatures in the list
    selected_monatures = monatures[0:party_size]
     
  # Remove the monatures that have been selected,
  # so they can't be selected by another competitor
  for selected_monature in selected_monatures:
    monatures.remove(selected_monature)
 
  return selected_monatures

@dataclass
class Monature:
   name: str
   strength: int
   flair: int
   speed: int


def load_monatures():
  monatures = []
  with open('monatures.json', 'r') as file:
    monatures = json.load(file)
    #print(monatures)
  monatures_list = [Monature(**value) for value in monatures['monatures']]
  #print(monatures_list)
  return(monatures_list)
  
   
def player_won_battle(player_monature, enemy_monature, battle_type):
  if battle_type == ARM_WRESTLE:
     if player_monature.strength > enemy_monature.strength:
       return PLAYER_WON
     elif player_monature.strength < enemy_monature.strength:
       return PLAYER_LOST
     else: 
       return TIE
  if battle_type == DANCE_OFF:
    if player_monature.flair > enemy_monature.flair:
       return PLAYER_WON
    elif player_monature.flair < enemy_monature.flair:
       return PLAYER_LOST
    else: 
       return TIE
  if battle_type == RACE:
    if player_monature.speed > enemy_monature.speed:
       return PLAYER_WON
    elif player_monature.speed < enemy_monature.speed:
       return PLAYER_LOST
    else: 
       return TIE


def output_parties(player_monatures, enemy_monatures):
  #round_times =+1
  #print(f"Round {round_times}")
  player_monatures_names = ", ".join([player_mona.name for player_mona in player_monatures])
  enemy_monatures_names = ", ".join([enemy_mona.name for enemy_mona in enemy_monatures])
  return f"{player_monatures_names} vs {enemy_monatures_names}"


if __name__ == "__main__":
 
  random_select = input("Random monatures?: ")
  random_select = random_select == "y"
  #print(random_select)
 
  # These lines of code will select the monatures that will compete
  # with each other, once the functions are implemented
  monatures = load_monatures()
  player_monatures = select_monatures(monatures, 3, random_select)
  enemy_monatures = select_monatures(monatures, 3, random_select)
  #print(player_monatures)
  #print(enemy_monatures)
  # Your code to implement the rounds and battles should go here
  round_times = 0
  while len(player_monatures)!=0 and len(enemy_monatures)!=0:
    round_times += 1
    #print(round_times)
    print(f"Round {round_times}")
    start_stat = output_parties(player_monatures, enemy_monatures)
    print(start_stat)
    print("=====")
    print()
    battle_time = 0

    battle_time +=1
    print(f"Battle {battle_time}")
    print("-----")
    battle_type = random_battle_type()
    player_monature = player_monatures[0]
    enemy_monature = enemy_monatures[0]
    round_result = player_won_battle(player_monature, enemy_monature, battle_type)

    while round_result == TIE:
      print(f"Your {player_monature.name} tied with the enemy's {enemy_monature.name} in a {battle_type}.")
      print()
      battle_time +=1
      print(f"Battle {battle_time}")
      print("-----")
      battle_type = random_battle_type()
      player_monature = player_monatures[0]
      enemy_monature = enemy_monatures[0]
      round_result = player_won_battle(player_monature, enemy_monature, battle_type)
      

    if round_result == PLAYER_WON:
      print(f"Your {player_monature.name} beat the enemy's {enemy_monature.name} in a {battle_type}.")
      print()
      enemy_monatures.remove(enemy_monature)
    elif round_result == PLAYER_LOST:
      print(f"Your {player_monature.name} lost to the enemy's {enemy_monature.name} in a {battle_type}.")
      print()
      player_monatures.remove(player_monature)

  if len(player_monatures) == 0:
    print("You lost!")
  else:
    print("You win!")
  



