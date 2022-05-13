def fun3(x):
    if x>0:
        print(x)
        fun3(x-1)


def fun4(x):
    if x>0:
        fun4(x-1)
        print(x)


# fun3(3)
fun4(3)
