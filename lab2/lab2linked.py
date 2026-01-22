from linkedQFile import LinkedQ

if __name__ == "__main__":

    # Rätta svaret: 7, 1, 12, 2, 8, 3, 11, 4, 9, 5, 13, 6, 10
    input_list = input("Skriv in dina objekt med mellanslag som separator:\n").split()

    Q = LinkedQ()

    Q.mega_enqueue(input_list)

    tmpans = LinkedQ()
    state = 0

    while True:
        if Q.isEmpty():
            break
        if state == 0:
            tmp = Q.dequeue()
            Q.enqueue(tmp)
            state = 1
        else:
            tmpans.enqueue(Q.dequeue())
            state = 0
    
    my_list = tmpans.show()
    print(" ".join(my_list))
