#include <bits/stdc++.h>
using namespace std;
int a[1000005];
int main()
{
	int n;
	string s;
	cin>>n>>s;
	s=s+s;
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<2;j++)
		{
			a[0]=i;
			a[1]=j;
			for(int i=2;i<=n+1;i++)
			{
				if(s[i-1]=='o'&&a[i-1]==0)
					a[i]=1-a[i-2];
				if(s[i-1]=='o'&&a[i-1]==1)
					a[i]=a[i-2];
				if(s[i-1]=='x'&&a[i-1]==0)
					a[i]=a[i-2];
				if(s[i-1]=='x'&&a[i-1]==1)
					a[i]=1-a[i-2];
			}
			if(a[n]==a[0]&&a[n+1]==a[1])
			{
				for(int i=0;i<n;i++)
				{
					if(a[i])
						cout<<'S';
					else
						cout<<'W';
				}
				return 0;
			}
		}
	}
	cout<<"-1";

	return 0;
}