#include<bits/stdc++.h>
using namespace std;
int a[100005];
int main()
{
	int n,t;
	cin>>n>>t;
	int minn=1e9;
	int manx=0;
	for(int i=1;i<=n;++i)
	{
		cin>>a[i];
		minn=min(minn,a[i]);
		manx=max(manx,a[i]-minn);
	}
	int ans=0;
	minn=1e9;
	for(int i=1;i<=n;++i)
	{
		minn=min(minn,a[i]);
		if(a[i]-minn==manx) ans++;
	}
	cout<<ans<<endl;
	return 0;
}