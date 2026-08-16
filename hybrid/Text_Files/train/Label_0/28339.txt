#include<bits/stdc++.h>
using namespace std;
int a[300001],b[300001]={0},c[300001]={0};
int u=0;
int n;
int k;
int judge(int q,int k)
{
	int l=1,r=n,mid,ans;
	while(l<=r)
	{
		mid=(l+r)/2;
		if(b[mid]<q&&(mid==n||b[mid+1]>=q))
		{
			ans=mid;
			break;
		}
		else if(b[mid]<q) l=mid+1;
		else r=mid-1;
	}
	if((n-ans)*q+c[ans]>=k*q) return 1;
	else return 0;
}
int main(){
	cin>>n;
	int m=-1;
	for(int i=1;i<=n;++i)
	{
		int x;
		cin>>x;
		b[x]++;
	}
	sort(b+1,b+n+1);
	for(int i=1;i<=n;++i)
	{
		c[i]=c[i-1]+b[i];
	}
	int q=n;
	for(int i=1;i<=n;++i)
	{
		while(!judge(q,i))
		{
			q--;
		}
		cout<<q<<endl;
	}
	return 0;
}