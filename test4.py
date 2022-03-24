"""
 * Project name(项目名称)：Python循环
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:45
 * Version(版本): 1.0
 * Description(描述)： Python 中，无论是 while 循环还是 for 循环，其后都可以紧跟着一个 else 代码块，
 它的作用是当循环条件为 False 跳出循环时，程序会最先执行 else 代码块中的代码。
 """

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    for i in list1:
        print(i, end=" ")
    else:
        print()
        print("执行else")
