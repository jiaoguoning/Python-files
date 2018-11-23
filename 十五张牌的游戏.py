import random

# 初始游戏
def init_game(lists):
    temp = []
    i = 0
    while i < 15:
        num = random.randint(1, 255)
        if num not in temp:
            temp.append(num)
            i = i + 1
    lists[0] = temp[0:5]
    lists[1] = temp[5:10]
    lists[2] = temp[10:15]
    print("=========================")
    print("请记住下列数字中的任选一个！")
    for i in range(len(temp)):
        print("%3d" % temp[i], end="  ")
        if i % 5 == 4:
            print("")
    print("=========================")


# 询问
def ask_player(lists):
    i = 0
    while i < 3:
        count = 0
        while count < 3:
            temp = []
            print(lists[count])
            answer = input("上面面是否有你选的数字（y/n）：")
            if answer == 'y':
                if count == 0:
                    temp.append(lists[count + 1])
                    temp.append(lists[count])
                    temp.append(lists[count + 2])
                elif count == 1:
                    temp.append(lists[count - 1])
                    temp.append(lists[count])
                    temp.append(lists[count + 1])
                elif count == 2:
                    temp.append(lists[count - 2])
                    temp.append(lists[count])
                    temp.append(lists[count - 1])
                # 重新发牌
                shuffle_card(temp, lists)
                break
            count += 1
        i += 1


# 发牌
def shuffle_card(temp, lists):
    lists[0] = []
    lists[1] = []
    lists[2] = []
    j = 0
    while j < 3:
        k = 0
        while k < 5:
            if (j * 5 + k) % 3 == 0:
                lists[0].append(temp[j][k])
            elif (j * 5 + k) % 3 == 1:
                lists[1].append(temp[j][k])
            elif (j * 5 + k) % 3 == 2:
                lists[2].append(temp[j][k])
            k += 1
        j += 1


num_lists = [[], [], []]
init_game(num_lists)
ask_player(num_lists)
print("你选择的数字是%d！" % num_lists[1][2])
