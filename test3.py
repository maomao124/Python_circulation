"""
 * Project name(项目名称)：Python循环
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/24 
 * Time(创建时间)： 20:39
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    str1 = "1234567890123456789012345678901234567890123456789012345678901234567890"
    for i in str1:
        print(i, end=" ")

    print()

    print("计算 1+2+...+100 的结果为：")
    # 保存累加结果的变量
    result = 0
    # 逐个获取从 1 到 100 这些值，并做累加操作
    for i in range(101):
        result += i
    print(result)

    list1 = [3, 5, 7, 9, 3, 12, 3]
    for i in list1:
        print(i, end=" ")

    print()

    dict1 = {"1": "11", "2": "22", "3": "33"}
    for i in dict1:
        print(i)
    for i in dict1.items():
        print(i)
    for i in dict1.keys():
        print(i)
    for i in dict1.values():
        print(i)
