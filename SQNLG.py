import random

TEST_TEXT = ["你好！","今天天气不错！","你吃饭了没？","现在几点了呀？","该下班了吧。"]

TEST_TEXT_LENGTH = len(TEST_TEXT)


# 按照查询进行对话
def single_sentence_gen():
    print(TEST_TEXT[random.randint(0,TEST_TEXT_LENGTH-1)])


