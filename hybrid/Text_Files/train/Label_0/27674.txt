#include<bits/stdc++.h>
using namespace std;
long long a,n,k[100005],ans=999999999999999;
int main()
{
	cin>>a>>n;
	for(int s=1;s<=a;s++)
	{
		cin>>k[s];
		if(s>=n)
		{
			if(k[s]<=0&&k[s-n+1]<=0)
			ans=min(ans,-k[s-n+1]);
			if(k[s]>0&&k[s-n+1]<=0)
			ans=min(ans,min(k[s]-k[s-n+1]*2,k[s]*2-k[s-n+1]));
			if(k[s]>=0&&k[s-n+1]>=0)
			ans=min(ans,k[s]);
		}
	}
	cout<<ans<<endl;
}