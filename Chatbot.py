import nltk
nltk.download('punkt')

from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"我的名字是(.*)",
        ["你好，%1！", "你好，%1，有什么我可以帮助你的吗？"]
    ],
    [
        r"你叫什么名字",
        ["我是一个简单的机器人", "你可以叫我机器人"]
    ],
    [
        r"你来自哪里",
        ["我来自计算机世界"]
    ],
    [
        r"退出",
        ["再见，希望能再次帮助你！", "再见！"]
    ]
]

def chatbot():
    print("你好！我是一个简单的机器人。输入'退出'可以退出对话。")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
