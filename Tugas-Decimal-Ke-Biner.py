from collections import deque

print("NAMA           : Muhamad Rizki Daelami")
print("NIM            : 2211310046")
print("KELAS          : 2C (wekeend)")
print("PORDI          : Teknologi Informasi")
print("DOSEN PENGAMPU : Ahmad Deni Muttaqin, S.Kom., M.Sc")
print("=" * 50)


# Fungsi untuk mengubah bilangan desimal ke biner
def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"

    # Menggunakan deque sebagai stack
    stack = deque()
    while decimal > 0:
        remainder = decimal % 2
        stack.append(remainder)
        decimal = decimal // 2

    # Menggunakan deque sebagai LIFO Queue
    lifo_queue = deque()
    while len(stack) > 0:
        lifo_queue.append(stack.pop())

    # Menggunakan deque sebagai queue
    queue = deque()
    while len(lifo_queue) > 0:
        queue.append(lifo_queue.popleft())

    binary = "".join(str(digit) for digit in queue)
    return binary


# Menerima input bilangan desimal
decimal = int(input("Masukkan bilangan desimal: "))

# Mengubah bilangan desimal ke biner
binary = decimal_to_binary(decimal)
print("Biner:", binary)
