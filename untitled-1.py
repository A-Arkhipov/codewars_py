string = "BEsCZWxNVz"
my_list = list(string)
my_set = set(string)
print(len(my_list) == len(my_set))
print (my_list, my_set)

array = list(filter(lambda el: string.lower().count(el) > 1, string.lower()))
print(array)
print(len(array) == 0)