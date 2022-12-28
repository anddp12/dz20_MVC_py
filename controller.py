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
        message = m.check(s)
        v.viewMassage(message)

def main():
    v.viewMassage('Сыграем в игру кости')
    f = controller()

if __name__ == '__main__':
    main()
