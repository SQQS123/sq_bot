from SQNLP import forward_longest_match, backwards_longest_match
from SQNLG import single_sentence_gen


"""
开发者学：尽量避免通过概率来完成任务，我们说话也不是通过概率来决定下一个词的
前期通过听我们自问自答使该机器人自主学习语言
我们学习的时候是几种感官协同学习的，但是目前我水平还达不到能让计算机同时学习，多以先从聊天学习开始
目前聊天不要尝试试图让计算机理解每个词汇的意思，只需要大概让计算机知道词汇的相互关系
希望她能从聊天的内容中学到一些信息并能够永久存储
"""


class Brain(object):
    def __init__(self):
        self.words_mem = []
        self.sentences_mem = []
        pass

class Robot(object):
    def __init__(self):
        self.brain = Brain()
        self.brain.sentences_mem = open('sentences_mem.txt','r',encoding='utf-8').read().split('\n')
        pass
    
    # 思考：有常用词语的语料文件，那我们还需不需要下面这个学习词汇的功能呢？
    # 果长期来看的话，可以让她实现低频词汇的自动废弃。
    def study_vocab(self):
        while True:
            word = input("请输入词语，输入'quit'退出:\n")
            if word == 'quit':
                return
            else:
                # 将学到的词语存储到机器人的神经元中，目前先使用list存储
                self.brain.words_mem.append(word)


    def study_sentence(self):
        while True:
            sentence = input("请输入一些句子，输入'quit'退出:\n")
            if sentence == 'quit':
                return
            else:
                # 将学到的词语存储到机器人的神经元中，目前先使用list存储
                with open('./sentences_mem.txt','a',encoding='utf-8') as f:
                    f.write(sentence+'\n')

    def study(self):
        pass

    def study_feedback(self):
        pass

    def see(self):
        pass

    def listen(self):
        """
        语音识别
        """
        pass

    def talk(self):
        """
        语音合成
        """
        pass

    def chat(self):
        """
        自然语言生成NLG
        """
        while True:
            question = input()
            if question=='你叫什么':
                print('我叫李罢')
            elif question=='q' or question == 'Q':
                return 0


def main():
    robot = Robot()
    # print(robot.brain.sentences_mem)
    robot.study_sentence()


if __name__=='__main__':
    main()
