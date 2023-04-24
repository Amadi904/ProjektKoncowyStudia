import random
import time
#Wylosować [10000] liczb całkowitych z zakresu: <65, 91>: zapisać w tablicy text

def Losowanie(text):
    for i in range(10000):
        num = random.randint(65, 91)
        text.append(num)
    print(text)
    return text



# Wylosować [5] liczb całkowitych z zakresu: <65, 90>: zapisać w tablicy pattern
def LiczbyLosowe():
    pattern = []
    for i in range(5):
        num = random.randint(65, 90)
        pattern.append(num)
    print(pattern)
    return pattern

#Wyczyścić tablicę text z wartości [91] za pmocą:
#Copy-over algorithm
def CopyOver(unique_data):
    TablicaPosortowana = []
    for i in range(len(tablica)):
        if tablica[i] !=91:
            TablicaPosortowana.append(tablica[i])
    print("Dane po zastosowaniu algorytmu Copy Over:")
    print(TablicaPosortowana)
    return TablicaPosortowana



#Converging pointers algorithm
def converging_pointers_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        left += 1

    # Usuwanie duplikatów
    i = 0
    while i < n - 1:
        if arr[i] == arr[i + 1]:
            del arr[i]
            n -= 1
        else:
            i += 1
#Wyszukać wartość wylosowaną z zakresu <65, 90> za pomocą,(pamiętając
# o tym, że należy wcześniej posortować za pomocą marge sort :)
#Linear search algorithm
#Binary Search algorithm
#posortowane dane za pomoca marge sort
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_arr = data[:mid]
        right_arr = data[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                data[k] = left_arr[i]
                i += 1
            else:
                data[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            data[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            data[k] = right_arr[j]
            j += 1
            k += 1
#wyszukanie danych za pomoca algorytmow
#Binary Search algorithm
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
# Linear search algorithm
def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1
#Zamienić wartości numeryczne na tekstowe (ASCII) i
# wyszukać w tablicy text wzoru – pattern za pomocą algorytmu: kmp Boyer Moore Algorithm
def ZamianaLiczb(array):
    # zamiana na tekstowe (ASCII)
    text_arr = [chr(num) for num in array]
    text = "".join(text_arr)
    print(text)
def compute_lps(pattern):
    """
    Funkcja zwraca tablicę LPS (Longest Proper Prefix Suffix) dla wzorca.
    """
    lps = [0] * len(pattern)
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps
def kmp_search(text, pattern):
    """
    Funkcja zwraca listę indeksów, na których zaczyna się wzorzec w tekście.
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0  # indeks w tekście
    j = 0  # indeks w wzorcu
    indices = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return indices
#P.S. Wyszukiwanie z pkt. 4 i 6 powinno podać wszystkie wystąpienia
# wyszukiwanej wartości w tablicy z liczbami lub w tekście.
# start = time.time()
    binary_search()
    end = time.time()

    start = time.time()
    linear_search()
    end = time.time()
if __name__ == "__main__":

    tablica=[]
    Los=Losowanie(tablica)
    LIczbylosowe=LiczbyLosowe()
    sortowanie=CopyOver(tablica)
