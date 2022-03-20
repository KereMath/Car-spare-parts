def calculate_price(part_list):
    elements = []
    initial = []
    tree = []
    if len(part_list)==0:
        return 0
    if len(part_list)==1:
        tree.append(part_list[0][0])
        return part_list[0][1]
    if len(part_list)>1:
        for i in range(len(part_list)):
            elements.append(part_list[i][0])
        for j in range(len(part_list)):
            for i in range(len(part_list[j])):
                for k in elements:
                    if len(part_list[j]) > 2:
                        if type(part_list[j][i])==type((1,2)):
                            if k == part_list[j][i][1]:
                                initial.append(k)
                    if len(part_list[j]) == 2:
                        if type(part_list[j][1])==type((1,2)):
                            initial.append(part_list[j][1][1])
        for i in range(len(elements)):
            if elements[i] in initial:
                pass
            else:
                tree.append(elements[i])
        for i in range(len(tree)):
            if tree[i] in elements:
                elements.remove(tree[i])
        def appendchild(L):
            for i in range(len(L)):
                if type(L[i]) == type('bike'):
                    for j in range(len(part_list)):
                        if L[i] == part_list[j][0]:
                            if type(part_list[j][1])==type((1,2)):
                                for k in range(1, len(part_list[j])):
                                    if type(part_list[j][k][1]) == type('bike'):
                                        if part_list[j][k][1] in elements:
                                            L.append([part_list[j][k][0], part_list[j][k][1]])
                                            elements.remove(part_list[j][k][1])
                if type(L[i]) == type([1, 2]):
                    appendchild(L[i])
            return L
        while elements:
            appendchild(tree)
        def howmany(L, thing):
            sum = 0
            if type(L) == type([1, 2]):
                if len(L) == 2:
                    if L[1] == thing:
                        return L[0]
                    else:
                        return howmany(L[1], thing)
                if len(L) > 2:
                    if type(L) == type([1, 2]):
                        for i in range(len(L)):
                            if type(L[0]) == type(3):
                                a = L[0] * howmany(L[i], thing)
                                sum += a
                            else:
                                a = howmany(L[i], thing)
                                sum += a
            return sum
        sum1 = 0
        for i in range(len(part_list)):
            if len(part_list[i]) == 2:
                k=part_list[i][1] * howmany(tree, part_list[i][0])
                if type(k)==type(9.1):
                    sum1 += part_list[i][1] * howmany(tree, part_list[i][0])

        return sum1

def required_parts(part_list):
    elements = []
    initial = []
    tree = []
    if len(part_list)==0:
        return []
    if len(part_list)==1:
        tree.append(part_list[0][0])
        return (1,tree[0])
    if len(part_list)>1:
        for i in range(len(part_list)):
            elements.append(part_list[i][0])
        for j in range(len(part_list)):
            for i in range(len(part_list[j])):
                for k in elements:
                    if len(part_list[j]) > 2:
                        if type(part_list[j][i]) == type((1, 2)):
                            if k == part_list[j][i][1]:
                                initial.append(k)
                    if len(part_list[j]) == 2:
                        if type(part_list[j][1]) == type((1, 2)):
                            initial.append(part_list[j][1][1])
        for i in range(len(elements)):
            if elements[i] in initial:
                pass
            else:
                tree.append(elements[i])
        for i in range(len(tree)):
            if tree[i] in elements:
                elements.remove(tree[i])

        def appendchild(L):
            for i in range(len(L)):
                if type(L[i]) == type('bike'):
                    for j in range(len(part_list)):
                        if L[i] == part_list[j][0]:
                            if type(part_list[j][1]) == type((1, 2)):
                                for k in range(1, len(part_list[j])):
                                    if type(part_list[j][k][1]) == type('bike'):
                                        if part_list[j][k][1] in elements:
                                            L.append([part_list[j][k][0], part_list[j][k][1]])
                                            elements.remove(part_list[j][k][1])
                if type(L[i]) == type([1, 2]):
                    appendchild(L[i])
            return L

        while elements:
            appendchild(tree)

        def howmany(L, thing):
            sum = 0
            if type(L) == type([1, 2]):
                if len(L) == 2:
                    if L[1] == thing:
                        return L[0]
                    else:
                        return howmany(L[1], thing)
                if len(L) > 2:
                    if type(L) == type([1, 2]):
                        for i in range(len(L)):
                            if type(L[0]) == type(3):
                                a = L[0] * howmany(L[i], thing)
                                sum += a
                            else:
                                a = howmany(L[i], thing)
                                sum += a
            return sum
        elements1=[]
        newList=[]
        for i in range(len(part_list)):
            elements1.append(part_list[i][0])
        for i in range(len(elements1)):
            if howmany(tree,elements1[i])!= 0 :
                newList.append([howmany(tree,elements1[i]),elements1[i]])
        for i in range(len(newList)):
            newList[i]=tuple(newList[i])
        return newList


def stock_check(part_list, stock_list):
    needed= required_parts(part_list)
    shortage=[]
    objects=[]
    toremove=[]
    for i in range(len(stock_list)):
        objects.append(stock_list[i][1])
    for i in range(len(needed)):
        if needed[i][1] in objects:
            for j in range(len(stock_list)):
                if needed[i][1]==stock_list[j][1]:
                    list(needed[i])
                    k=needed[i][0]-stock_list[j][0]
                    shortage.append((k,needed[i][1]))
        else:
            shortage.append(((needed[i][0],needed[i][1])))
    for k in range(len(shortage)):
        if shortage[k][0] <= 0:
            toremove.append(shortage[k])
    for o in range(len(toremove)):
        c=shortage.index(toremove[o])
        shortage.remove(shortage[c])
    for i in range(len(shortage)):
        shortage[i]=list(shortage[i])
        shortage[i][0],shortage[i][1]=shortage[i][1],shortage[i][0]
        shortage[i]=tuple(shortage[i])
    return shortage
