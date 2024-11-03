items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def FindMyProduct(a, b):
    for i in range(len(a)):
        if(a[i] == b):
            return i
    return None



for find_item in ['банан', 'груша', 'персик']:
    index_item = FindMyProduct(items_list, find_item)  
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")


