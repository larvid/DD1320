from ArrayQFile import *

if __name__ == "__main__":
    Q = ArrayQ()

    for i in range(1,14):
        Q.enqueue(i)
    

    for j in range(9):
        state = 0
        tmpans = array('i',[])

        while True:
            if Q.isEmpty():
                print(tmpans)
                break
            if state == 0:
                tmp = Q.dequeue()
                Q.enqueue(tmp)
                state = 1
            else:
                tmpans.append(Q.dequeue())
                state = 0

        Q._Q = tmpans

"""
Q = ArrayQ()
Q.enqueue(1)
Q.enqueue(2)
print(Q.isEmpty())
Q.dequeue()
Q.dequeue()
print(Q.isEmpty())
print(len(Q._Q))
"""