

class Robot(object):
    def __init__(self):
        pass

    def see(self):
        pass

    def listen(self):
        pass

    def talk(self):
        pass

    def chat(self):
        while True:
            question = input()
            if question=='你叫什么':
                print('我叫李罢')
            elif question=='q' or question == 'Q':
                return 0


def main():
    robot = Robot()
    robot.chat()

if __name__=='__main__':
    main()