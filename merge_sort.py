def merge_sort(data_item):
    if len(data_item) > 1:
        mid = len(data_item) // 2
        left = data_item[:mid]
        right = data_item[mid:]

        merge_sort(left)
        merge_sort(right)


        i, j, k = 0, 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data_item[k] = left[i]
                i += 1
            
            else:
                data_item[k] = right[j]
                j += 1
            
            k += 1

        while i < len(left):
            data_item[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            data_item[k] = right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    data_item = [12, 4, 5, 10, 15, 20]
    print("Before sorted list:", data_item)
    merge_sort(data_item)
    print("After sorted list:", data_item)