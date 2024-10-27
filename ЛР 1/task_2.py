SIZE_DISK = 1.44 * 1024 * 1024
NUM_PAGES = 100
NUM_STR = 50
NUM_CHAR = 25
SIZE_CHAR = 4

size_book = NUM_PAGES * NUM_STR * NUM_CHAR * SIZE_CHAR
num_book = SIZE_DISK // size_book
print(f"Количество книг, помещающихся на дискету: {num_book:.0f}")
