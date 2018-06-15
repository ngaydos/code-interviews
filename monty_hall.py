import random

def non_switched():
    selection = 1
    correct_door = random.randint(1, 3)
    return selection == correct_door

def switched():
    correct_door = random.randint(1, 3)
    if correct_door == 2 or correct_door == 3:
        return True
    else:
        return False

if __name__ == '__main__':
    switched_wins = 0
    non_switched_wins = 0
    for x in range(1000000):
        switched_wins += (switched())
        non_switched_wins += (non_switched())
    print('switched wins: ' + str(switched_wins/10000))
    print('non switched wins: ' + str(non_switched_wins/10000))