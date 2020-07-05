#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <string>
#include <cstring>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <ctime>
#include <vector>
#include <fstream>
#include <list>
#include <iomanip>
#include <numeric>
#define init(array) memset(array,0,sizeof(array))
#define mal(array,type,size) type*array=(type*)malloc(sizeof(type)*size);
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
const int inf = 0x3f3f3f3f;



int board[10][10] = {{0}};//存数独棋盘,方便起见，只用1-9角标
struct triplet//每个格子
{
	int r, f, n;//行、列、数字
	triplet(int rr, int ff, int nn)
	{
		r = rr, f = ff, n = nn;
	}
	triplet(const triplet &t)
	{
		this->r = t.r, this->f = t.f, this->n = t.n;
	}
};

void readBoard()
{
  	string a;
  	for (int i = 1; i <= 9; ++i)
  	{
      	getline(cin,a);
      	for (int j = 0; j < 9; ++j)
      	{
          	board[i][j + 1] =  a[j] - '0';
      	}
  	}
}

void showCurrent()
{
	cout << endl;
  	for (int i = 1; i <= 9; ++i)
  	{
  	    for (int j = 1; j <= 9; ++j)
          	cout << board[i][j];
  	    cout << endl;
  	}
  	cout << endl;
}

bool check(int r,int f,int n)//检查r行f列能否放n
{
  	for (int i = 1; i <= 9; ++i)
  	{
   	 	if(board[r][i] == n) return false;
   	 	if(board[i][f] == n) return false;
   	 	if(board[3 * ((r - 1) / 3) + ((i - 1) / 3) + 1][3 * ((f - 1) / 3) + ((i - 1) % 3) + 1] == n) return false;
 	}
  	return true;
}

bool findNext(stack<triplet>& s)
{
	int rr = s.top().r, ff = s.top().f;
	//找到最后了已经
	if(rr > 9 || ff > 9) return false;
	while(true)
	{
		//向后找
		if(ff == 9) rr++, ff = 1;
		else ff++;
		//找到最后了已经
		if(rr > 9 || ff > 9) return false;
		//跳过已经有的数
		if(board[rr][ff] > 0) continue;
		//找到一个空格子，找第一个合适的数填上,并加入搜索栈
		for (int i = 1; i <= 9; ++i)
		{
			if(check(rr,ff,i))
			{
				s.push(triplet(rr,ff,i)), board[rr][ff] = i;
				return true;
			}
		}
		//到这还没退出，这说明当前栈里的结果已经找不到下一个了，得出栈一些东西了
		//temp为当前考察的栈顶元素
		triplet temp(s.top());
		while(true)
		{
			//题目保证不会出现找不到下一个的情况；
			if(s.empty()) return false;
			//若当前已经搜到9了，出栈再考察前一个
			if(temp.n == 9) 
			{
				board[temp.r][temp.f] = 0;
				s.pop();
				temp = s.top();
				continue;
			}
			//否则考察下一个
			if(check(temp.r, temp.f, ++temp.n))
			{
				s.pop();
				s.push(temp);
				board[temp.r][temp.f] = temp.n;
				return true;
			}
		}
		rr = s.top().r, ff = s.top().f;
	}
	return true;
}

int main(int argc, char * argv[]) 
{
    //初始化
	readBoard();	
	stack<triplet> s;
	s.push(triplet(1,0,0));//虚拟的初始节点
	while(findNext(s)) ;//不必做什么
	cout << endl << "答案是：";
	showCurrent();	
    return 0;
}