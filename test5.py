"""
 * Project name(项目名称)：Python循环
 * Package(包名): 
 * File(文件名): test5
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:49
 * Version(版本): 1.0
 * Description(描述)： 循环嵌套
 当 2 个（甚至多个）循环结构相互嵌套时，位于外层的循环结构常简称为外层循环或外循环，位于内层的循环结构常简称为内层循环或内循环。
循环嵌套结构的代码，Python 解释器执行的流程为：
当外层循环条件为 True 时，则执行外层循环结构中的循环体；
外层循环体中包含了普通程序和内循环，当内层循环的循环条件为 True 时会执行此循环中的循环体，直到内层循环条件为 False，跳出内循环；
如果此时外层循环的条件仍为 True，则返回第 2 步，继续执行外层循环体，直到外层循环的循环条件为 False；
当内层循环的循环条件为 False，且外层循环的循环条件也为 False，则整个嵌套循环才算执行完毕。
 """

if __name__ == '__main__':
    i = 0
    while i < 10:
        for j in range(10):
            print("i=", i, " j=", j)
        i = i + 1

    print()
    i = 0
    if i < 10:
        for j in range(5):
            print("i=", i, " j=", j)
