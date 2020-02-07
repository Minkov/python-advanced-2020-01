# # def f_args(*args):
# #     if not args:
# #         print(None)
# #         return
# #
# #     current_min = args[0]
# #     for x in args:
# #         if x < current_min:
# #             current_min = x
# #
# #     print(current_min)
# #
# #
# # def f_kwargs(**kwargs):
# #     print(kwargs['name'])
# #     print(kwargs)
# #
# #
# # def my_min(x, *args):
# #     current_min = x
# #     for x in args:
# #         if x < current_min:
# #             current_min = x
# #
# #     return current_min
# #
# #
# # def f(x, **kwargs):
# #     print(x)
# #     print(kwargs)
# #
# #
# # def f2(*args, **kwargs):
# #     print(args)
# #     print(kwargs)
# #
# #
# # def f3(x, y, *args, **kwargs):
# #     print(x)
# #     print(y)
# #     print(args)
# #     print(kwargs)
# #
# #
# # # f2(1, name='Pesho', age=11)
# # f3(1, 2, 3)
# #
# # # f_args(1, 2, 3, 4, -5, 6, 1)
# # # f(1)
# # # f()
# #
# #
# # print(my_min(1) == 1)
# # print(my_min(1, 2, -5) == -5)
# # print(my_min(1, 2, 11111, -5) == -5)
#
#
# def my_min2(x, *args):
#     current_min = x
#     for x in args:
#         if x < current_min:
#             current_min = x
#
#     return current_min
#
#
# numbers = [1, 2, 3]
#
# print(my_min2(*numbers))


def f(**kwargs):
    print(kwargs)


options = {
    'db': {
        'CONNECTION_STRING': '......',
        'USER': 'Pesho',
        'PASSWORD': '123456qwe',
    },
}


def setup(db, *args, **kwargs):
    print(db)
    print(kwargs)

    next_fun(my_parameter, *args, **kwargs)


setup(**options)

d = {'name': 'Pesho', 'age': 13}

# f(**d)
# f(name=d['name'], age=d['age'])
