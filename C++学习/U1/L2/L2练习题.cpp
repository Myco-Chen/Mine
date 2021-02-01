//1.1 3
//2.TFTFT
//3.BDC
//4.4
#include <iostream>
using namespace std;
int main()
{
    int a, b;          //使用整数变量a,b前未定义
    cin >> a >> b;     //io流符号反了
    cout << a *b / 3;  //整数求商符号应为“/”
    return 0;
}