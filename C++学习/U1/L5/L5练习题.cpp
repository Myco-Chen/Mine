//1.1 3 5 7 9
//2.DCCC
//3.100,34,haha,
//4.i+=2
//5.
#include <iostream>
using namespace std;
int main()
{
    int n;//n在读取输入内容前未被定义
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cout << i *i << endl;//要的是i的平方，如果是n，则每次
    }                        //输出的内容都一样
    return 0;
}