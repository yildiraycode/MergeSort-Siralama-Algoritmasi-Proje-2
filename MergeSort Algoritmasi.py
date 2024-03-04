#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mergeSort(arr):
    if len(arr) > 1:
 
         # Dizinin ortasını bulma
        mid = len(arr)//2
 
        # Dizi elemanlarını bölme
        L = arr[:mid]
        # iki yarıya bölme
        R = arr[mid:]
 
        # İlk yarısını sıralama
        mergeSort(L)
 
        # İkinci yarısını sıralama
        mergeSort(R)
 
        i = j = k = 0
 
        # Verileri geçici dizilere kopyala L[] ve R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Herhangi bir elemanın kalmış olup olmadığını kontrol et
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
 
# Listeyi yazdırmak için kod
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
# Ana Kod
if __name__ == '__main__':
    arr = [16, 21, 11, 8, 12, 22]
    print("Verilen dizi")
    printList(arr)
    mergeSort(arr)
    print("\nSıralanmış dizi")
    printList(arr)
#Time Complexitiy:Big-O gösterimi :O(nLogn)

