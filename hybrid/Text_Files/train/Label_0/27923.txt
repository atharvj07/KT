#include<bits/stdc++.h>
using namespace std;
bitset<2000001>a;
int n,x,c;
int main()
{
	int i;
	cin>>n;
	a[0]=1;
	for(i=1;i<=n;i++)
	{
		cin>>x;
		c+=x;
		a|=a<<x;
	}
	for(i=c/2+c%2;i<=c;i++)
	{
		if(a[i]>0)
		{
			cout<<i<<endl;
			return 0;
		} 
	}
	return 0;	
} 