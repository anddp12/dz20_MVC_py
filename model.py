from random import randint

def cube(end=6):
    return randint(1, end)

def score(score, cube):
    if cube == 6:
        score += 3
        return score
    elif cube != 6:  
        score -= 1
        return score

def check(score):
    if score == 0:
        return 'Вы проиграли', False
    elif score > 0:
        return 'Вы еще в игре', True