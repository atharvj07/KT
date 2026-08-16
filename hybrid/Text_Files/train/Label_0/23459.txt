#include<bits/stdc++.h>
using namespace std;
int a[200001],b[200001];
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	cin>>a[i];
	for(int i=n;i>=1;i--)
	cin>>b[i];
	int flag=0;
	for(int i=1;i<=n;i++)
	{
		if(a[i]==b[i])
		{
			flag=0;
			for(int j=1;j<=n;j++)
			{
				if(a[i]!=b[j]&&a[j]!=b[i])
				{
					swap(b[i],b[j]);
					flag=1;
					break;
				}
			}
			if(!flag)
			{
				cout<<"No"<<endl;
				return 0;
			}
		}
	}
	cout<<"Yes"<<endl;
	for(int i=1;i<=n;i++)
	cout<<b[i]<<" ";
	return 0;
}
