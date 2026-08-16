#include <bits/stdc++.h>
using namespace std;
char s[100005];
bool t[100005];
int main()
{
	int n;
	cin>>n>>s;
	s[0];
	for(int i=0;i<2;i++)
	{
		for(int j=0;j<2;j++)
		{
			t[0]=i;
			t[1]=j;
			for(int k=1;k<n-1;k++)
				t[k+1]=t[k]^t[k-1]^(s[k]=='x');
			if((s[n-1]=='x')==t[n-2]^t[n-1]^t[0]&&(s[0]=='x')==t[n-1]^t[0]^t[1])
			{
				for(int k=0;k<n;k++)
				{
					if(t[k])
						cout<<'W';
					else
						cout<<'S';
				}
				return 0;
			}
		}
	}
	cout<<"-1";

	return 0;
}