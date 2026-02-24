class ChatBot:
    def __init__(self):
        self.rules = {}

    def add_rule(self, key, response):
        self.rules[key] = response

    def reply(self, text):
        for k in self.rules:
            if k in text.lower():
                return self.rules[k]
        return "Tushunmadim"

def run():
    bot = ChatBot()
    bot.add_rule("salom", "Salom bro!")
    bot.add_rule("qalesan", "Yaxshi, rahmat!")

    while True:
        t = input("Sen: ")
        if t == "exit":
            break
        print("Bot:", bot.reply(t))

run()
