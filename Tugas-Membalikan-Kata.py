from collections import deque

print("NAMA           : Muhamad Rizki Daelami")
print("NIM            : 2211310046")
print("KELAS          : 2C (wekeend)")
print("PORDI          : Teknologi Informasi")
print("DOSEN PENGAMPU : Ahmad Deni Muttaqin, S.Kom., M.Sc")
print("=" * 50)


def reverse_string(input_str):
    # Menggunakan deque
    deque_obj = deque()
    for char in input_str:
        deque_obj.append(char)
    membalik_str_deque = ""
    while len(deque_obj) > 0:
        membalik_str_deque += deque_obj.pop()

    # Menggunakan stack
    stack = []
    for char in input_str:
        stack.append(char)
    membalik_str_stack = ""
    while len(stack) > 0:
        membalik_str_stack += stack.pop()

    # Menggunakan LIFO queue
    queue = deque()
    for char in input_str:
        queue.append(char)
    membalik_str_lifoqueue = ""
    while len(queue) > 0:
        membalik_str_lifoqueue += queue.pop()

    return membalik_str_deque, membalik_str_stack, membalik_str_lifoqueue


input_str = input("Masukkan kata atau kalimat: ")
membalik_deque, membalik_stack, membalik_lifoqueue = reverse_string(input_str)

print("Hasil menggunakan deque:", membalik_deque)
print("Hasil menggunakan stack:", membalik_stack)
print("Hasil menggunakan LIFO queue:", membalik_lifoqueue)
