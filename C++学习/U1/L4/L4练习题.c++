//1.2 4 6 8 10 12
//2.ABCDD
//3.1:1 2 3 4 5
//3.2:1 4 9 16 25
//3.3:very very very nice!
//3.4:函数main1(),3.5:函数mian2()
#include <iostream>
#include <math.h>
using namespace std;
void main1(), main2();
int main()
{
    main1();
    main2();
    return 0;
}
void main1()
{
    cout << "ba";
    for (int i = 1; i <= 2; i++)
    {
        cout << "na";
    }
}
void main2()
{
    for (int i = 1; i <= pow(2, 7); i *= 2)
    {
        cout << i << " ";
    }
}