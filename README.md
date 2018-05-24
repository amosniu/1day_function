# global关键字的运用
在编写程序的时候，如果想为一个在函数外的变量重新赋值，并且这个变量会作用于许多函数中时，就需要告诉python这个变量的作用域是全局变量。此时用global语句就可以变成这个任务，也就是说没有用global语句的情况下，是不能修改全局变量的。
``` python
x = 6
def func1():
    global x
    x = 1
    print(x)
```
用print语句输出x的值，此时的全局变量x值被重新定义为1

python中的global语句是被用来声明是全局的，所以在函数内把全局变量重新赋值时，这个新值也反映在引用了这个变量的其它函数中。
``` python
def func2():
    return x
```
这里看到fun2函数return返回值是全局变量x，即返回1
