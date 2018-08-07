from cat import Cat
from mouse import Mouse
from person import Person
def main():
    ca = Cat('猫咪')
    # ca.eat()
    mou = Mouse('老鼠')
    # mou.eat()
    per = Person()
    per.feedcat(ca)
    per.feedmouse(mou)
if __name__ == '__main__':
    main()