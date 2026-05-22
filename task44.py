def common_elements(*lists):
    if not lists:
        return []
    
    f_list = lists[0]
    other_lists = lists[1:]

    result = []

    for element in f_list:
        is_common = True
        for lst in other_lists:
            if element not in lst:
                is_common = False
                break
        if is_common and element not in result:
            result.append(element)
    return result

print(common_elements([1,2,3,4], [3,2,4,6], [2,3,4]))