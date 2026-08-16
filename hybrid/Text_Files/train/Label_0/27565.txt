#include <bits/stdc++.h>
using namespace std;
int a,b,c,a1,b1,c1;
signed main()
{
    cin>>a>>b>>c;
	for(int i=0;;i++)
	{
		if(a&1||b&1||c&1)cout<<i,exit(0);
		if(a>b)swap(a,b);
		if(b>c)swap(b,c);
		if(a>b)swap(a,b);
		a1=(b+c)/2,b1=(a+c)/2,c1=(a+b)/2;
		a=a1,b=b1,c=c1;
		if(a==b&&b==c&&a==c)puts("-1"),exit(0);
	}
}