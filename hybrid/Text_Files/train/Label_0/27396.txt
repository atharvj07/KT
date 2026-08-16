#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
typedef long long ll;
const int N = 2e5+10;
int a[N];

int main()
{
    int t;
	cin>>t;
	while(t--)
	{
		int n;
		scanf("%d",&n);
		ll sum=0;
		int maxx=0;
		for(int i=0;i<n;i++) {
			scanf("%d",&a[i]);
			sum+=a[i];
			maxx=max(maxx,a[i]);
		}
		ll ans=1ll*maxx*(n-1)-sum;
		if(ans<0) ans+=(-ans)/(n-1)*(n-1);
		if(ans<0) ans+=n-1;
		printf("%lld\n",ans);
	} 
    return 0;
}