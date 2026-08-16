#include<bits/stdc++.h>
using namespace std;
const int N=2e5;
int a[N],mx[N],cnt,ans;
int main(){
	int n,t;
	scanf("%d%d",&n,&t);
	for (int i=1;i<=n;i++) scanf("%d",&a[i]);
	for (int i=n;(i);i--) mx[i]=max(mx[i+1],a[i]);
	for (int i=1;i<n;i++)
	{
		int o=mx[i]-a[i];
		if (o==ans) cnt++;
		if (o>ans)
		{
			ans=o;
			cnt=1;
		}
	}
	printf("%d",cnt);
}