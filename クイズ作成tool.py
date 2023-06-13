
mondai = input("1問目の問題文:")
選択1 = input("問題文1:")
sentaku2 = input("問題文2:")
sentaku3 = input("問題文3:")
sentaku4 = input("問題文4:")
kotae = input("答えを書いて！")

mondai2 = input("2問目の問題文:")
選択12 = input("問題文1:")
sentaku22 = input("問題文2:")
sentaku32 = input("問題文3:")
sentaku42 = input("問題文4:")
kotae2 = input("答えを書いて！")

mondai1 = input("3問目の問題文:")
選択11 = input("問題文1:")
sentaku21 = input("問題文2:")
sentaku31 = input("問題文3:")
sentaku41 = input("問題文4:")
kotae1 = input("答えを書いて！")

a = questions = [
    {
        "question": ""+mondai+"",
        "options": [""+選択1+"", ""+sentaku2+"", ""+sentaku3+"", ""+sentaku4+""],
        "answer": ""+kotae+""
    },
        {
        "question": ""+mondai2+"",
        "options": [""+選択12+"", ""+sentaku22+"", ""+sentaku32+"", ""+sentaku42+""],
        "answer": ""+kotae2+""
    },
    {
        "question": ""+mondai1+"",
        "options": [""+選択11+"", ""+sentaku21+"", ""+sentaku31+"", ""+sentaku41+""],
        "answer": ""+kotae1+""
    }
]
def ask_question(question, options):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    return int(input("回答番号を入力してください: "))

score = 0
for question in questions:
    answer = ask_question(question["question"], question["options"])
    if question["options"][answer - 1] == question["answer"]:
        score += 1
        print("正解です！")
    else:
        print("不正解です。")

print(f"あなたのスコアは {score} / {len(questions)} です。")