#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int h=0;
    int l=1,i,sum=0;
    for (i = 1; i <= n; i+=1)
    {
        sum += l*(i-h);
        l++;
        h=i;
    }
    if (i != n)
    {
        sum += (n-h)*1;
    }
    cout << sum << endl;
}