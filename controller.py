import model as m
import view as v

def controller():
    score = 100
    user = v.getChoise()
    if user == "s":
        cube = m.cube()
        print("🎲:", cube)
        s = m.score(score, cube)
        print("🧮:", s)
        message, result = m.check(score)
        v.viewMassage(message)

def main():
    v.viewMassage('Сыграем в игру кости')
    result = False
    v.getLoop()()

if __name__ == '__main__':
    main()
