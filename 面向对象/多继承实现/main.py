from son import Son

def main():
    s = Son(1000,123,999)
    s.play()
    s.eat()
    #父方法相同，调用继承时写括号前面的方法
    s.func()


if __name__ == '__main__':
    main()