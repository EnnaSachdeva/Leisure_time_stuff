import time
import sys


def access_list(sequence):
    start = time.time()
    x = sequence[0]
    print(time.time()-start)

    start = time.time()
    y = sequence[-1]
    print(time.time()-start)


    start = time.time()
    y = sequence[len(sequence)//2]
    print(time.time()-start)

    return x, y

def reverse(integer):
    output = 0

    start = time.time()
    while integer > 0:
        a = integer % 10
        output = (output *10) +a
        integer = integer // 10


    time_taken = time.time() - start

    return output, time_taken




def reverse_1(integer):
    start = time.time()

    output = list(str(integer))[::-1]

    output = int(''.join(output))

    time_taken = time.time() - start

    return output, time_taken

#print(sys.maxsize + 5)

#print(reverse(10010101010101010101010101010101010101010101010101000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)) #sys.maxsize))

#print(reverse_1(1001010101010101010101010101010101010101010101010101)) #sys.maxsize))


print(access_list(list(range(100000))))