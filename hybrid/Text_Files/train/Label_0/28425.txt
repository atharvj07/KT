#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,int> pli;
typedef pair<int,ll> pil;

const int INF = 1e9 ;
const int maxN = 1e5 + 5;

int n,m;
int a[maxN];
int b[maxN];
const int MOD = 1e9 + 7;
int main()
{
	scanf("%d%d",&n,&m);
	for(int i=1;i<=n;i++)
	{
		scanf("%d",&a[i]);
	}
	sort(a+1,a+1+n);
	reverse(a+1,a+1+n);
	for(int i=1;i<=m;i++)
	{
		scanf("%d",&b[i]);
	}
	sort(b+1,b+1+m);
	reverse(b+1,b+1+m);
	ll cnt = 1;
	int k1 = 0;
	int k2 = 0;
	for(int i = n*m;i>=1;i--)
	{
		if(a[k1+1] == i && b[k2+1] == i)
		{
			k1++;k2++;
			cnt *= 1;
			cnt %= MOD;
		}
		else if(a[k1+1] == i )
		{
			k1++;
			cnt *= k2;
			cnt %= MOD;
		}
		else if(b[k2+1] == i)
		{
			k2++;
			cnt *= k1;
			cnt %= MOD;
		}
		else
		{
			if ((ll)k1*k2 - (n*m - i) < 0)
				cnt = 0;
			else
				cnt *= ((ll)k1*k2 - (n*m - i));
			cnt %= MOD;
		}
	}
	printf("%lld\n",cnt);
	return 0;
} 