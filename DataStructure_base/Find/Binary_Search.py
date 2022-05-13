# def binary_search(li,val):
#     left =0
#     right = len(li)-1
#     while left<= right:
#         mid = (left+right)//2
#         if li[mid]==val:
#             return mid
#         elif li[mid]>val:
#             right = mid-1
#
#         else:
#             left = mid+1
#     else:
#
#         return None
# def linear_search(li,val):
#     for ind,v in enumerate(li):
#         if v == val:
#             return ind
#         else:
#             return None
# li = [1,2,3,4,5,6,7,8,9]
# print(binary_search(li,3))

##

data = [1,2,3,4,5,6,7,8]

#
# def binary_search(li,val):
#     low = 0
#     high = len(li)-1
#
#     while low <= high:###必须为小于等于
#         mid = (low + high) // 2
#         if li[mid]==val:
#             return mid
#
#         elif li[mid]>val:
#             high = mid-1
#
#         else:
#             low = mid+1
#     else:
#         return None
#
# print(binary_search(data,3))
def binary_search(li,val):
    low = 0
    high = len(li)-1

    
    while low<=high:
        mid = high+low
        if li[mid] == val:
            return mid
        elif li[mid]>val:
            high = mid-1

        else:
            low = mid+1

    else:
        return None


print(binary_search(data,3))

