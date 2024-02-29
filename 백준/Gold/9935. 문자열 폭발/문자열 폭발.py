def bomb(lst=[]):
    global bomb_word
    global bomb_lst
    # print(lst)
    for i in range(len(input_list)):
        bomb_lst.append(input_list[i])
        while len(bomb_lst)>=len(bomb_word):
            marker = False
            for i in range(len(bomb_word)):
                if bomb_lst[-1-i]!=bomb_word[-1-i]:
                    marker=True
                    break
            if marker:
                break
            else:
                for _ in range(len(bomb_word)):
                    bomb_lst.pop()
input_list = list(input())
# print(input_list)
bomb_word = list(input())
bomb_lst = []
bomb(input_list)
if len(bomb_lst) == 0:
    print("FRULA")
else:
    print(("").join(bomb_lst))