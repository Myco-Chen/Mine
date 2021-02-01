//1.16
//2.DCACB
//3.(1)：函数main1()
//3.(2)：(n % 5 == 0)
//3.(3)：函数main2()
//3.(4)：(x >= 18)
//3.(5)：bool a、b、c、d
#include <cstdio>
using namespace std;
void main1(), main2();
bool a = true;
bool b = false;
bool c = false;
bool d = true;
int main()
{
    main1();
    main2();
    return 0;
}
void main1()
{
    int n;
    printf("%s\n", "输入一个数:");
    scanf("%d", &n);
    if (n > 3)
    {
        printf("%s\n", "YES");
    }
}
void main2()
{
    int n;
    printf("%s\n", "输入木材总数：");
    scanf("%d", &n);
    if (n % 5 == 0)
    {
        printf("%d", n / 5);
    }
    else
    {
        printf("%d", n / 5 + 1);
    }
}
