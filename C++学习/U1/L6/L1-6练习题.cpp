//1.9
//2.CDDBA
//3.1:39
//3.2:28,26,24,22,20;
//3.3:函数main1()
//3.4:函数main2()
//3.5:函数main()
#include <iostream>
#include <cmath>
using namespace std;
void main1()
void main2()
int main()
{
    int n, x, sum = 0; //sum使用前未被定义
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        cin >> x;
        sum += x * x;//赋值+运算符号应为+=，并非+
    }
    cout << sum << endl;
    return 0;
}
void main1()
{
    int sum = 0;
    for (int i = 1; i <= 100; i++)
    {
        sum += i;
        cout << sum << " ";
    }
}
void main2()
{
    for (int i = 1; i <= sqrt(100); i++)
    {
        cout << i *i << " ";
    }
}