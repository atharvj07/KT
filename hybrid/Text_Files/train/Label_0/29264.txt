#include <bits/stdc++.h>
using namespace std;

int n;
string s,t;

int main()
{
	scanf("%d",&n);
	cin >> s >> t;
	for(int i=n;i >= 0;i--)
		if(s.substr(n-i) == t.substr(0,i))
		{	
			printf("%d\n",2*n-i);
			return 0;
		}
}