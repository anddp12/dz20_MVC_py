import model as m
import view as v

score = 100
def controller():
    global score
    user = v.getChoise()
    if user == "s":
        cube = m.cube()
        print("🎲:", cube)
        score = m.score(score, cube)
        print("🧮:", score)
        message, result = m.check(score)
        v.viewMassage(message)

def main():
    v.viewMassage('Сыграем в игру кости')
    result = False
    v.getLoop()()

if __name__ == '__main__':
    main()
