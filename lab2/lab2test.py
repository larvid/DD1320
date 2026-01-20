from linkedQFile import LinkedQ

if __name__ == "__main__":
    Q = LinkedQ()

    for i in range(1,14):
        Q.enqueue(i)
    
    print(Q)

    tmpans = []

    while True:
        if Q.isEmpty():
            break
        if state == 0:
            tmp = Q.dequeue()
            Q.enqueue(tmp)
            state = 1
        else:
            tmpans.append(Q.dequeue())
            state = 0
    
    print(tmpans)
