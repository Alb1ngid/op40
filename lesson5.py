#декораторы
def function(func):
    def wrapp(*args, **kwargs):
        print('чтото сделал ')
        res=func(*args,**kwargs)
        print('завершил результат ')
        return res
    return wrapp
@function
def les(*a,**b):
    print(f'адмирал:{b}')
    return f"вызов {a}"


# print(les("пяти",'адмиралов',маринфорд='акайну'))
les()

# @function
# def sumetime():
#     print('результат работы ')


# f=function(sumetime)
# f()

# sumetime()




