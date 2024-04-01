'''
색상이 주어진거임
2->4->6->8->10->12->23->21->2
1->3->5->7->9->11->24->22->1
'''
def complete(temp_lst):
    marker = True
    for i in range(6):
        st = set(temp_lst[4*i:4*(i+1)])
        if len(st)==1:
            continue
        else:
            marker=False
            break

    return marker
#큐브 완성되어 있나 체크

def rotate(temp_lst, rule={}):
    rot = dict()
    for k, v in rule.items():
        rot[v-1]=temp_lst[k-1]
    for k, v in rot.items():
        temp_lst[k]=v
    # print(temp_lst)
    return complete(temp_lst)


lst = list(map(int, input().split()))
rotate1 = {2:6, 4:8, 6:10, 8:12, 10:23, 12:21, 23:2, 21:4}
rotate2 = {v:k for k ,v in rotate1.items()}
rotate3 = {1:5, 3:7, 5:9, 7:11, 9:24, 11:22, 24:1, 22:3}
rotate4 = {v:k for k ,v in rotate3.items()}
rotate5 = {13:5, 14:6, 5:17, 6:18, 17:21, 18:22, 21:13, 22:14}
rotate6 = {v:k for k ,v in rotate5.items()}
rotate7 = {15 :7, 16:8, 7:19, 8:20, 19:23, 20:24, 23:15, 24:16}
rotate8 = {v:k for k ,v in rotate7.items()}
rotate9 = {3:17, 4:19, 17:10, 19:9, 10:16, 9:14, 16:3, 14:4}
rotate10 = {v:k for k ,v in rotate7.items()}
rotate11 = {1 :18, 2:20, 18:12, 20:11, 12:15, 11:13, 15:1, 13:2}
rotate12 = {v:k for k ,v in rotate7.items()}

rule=[]
rule.extend([rotate1,rotate2,rotate3,rotate4,rotate5,rotate6,rotate7,rotate8,rotate9,rotate10,rotate11,rotate12])
# print(*rule, sep='\n')
marker = False
for i in range(12):
    temp_lst = [j for j in lst]
    if rotate(temp_lst, rule[i]):
        marker = True
        break
if marker:
    print(1)
else:
    print(0)

