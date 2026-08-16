#include<cstdio>
#include<cstdlib>
#define maxn 200005
#define maxm 50000005
#define p 1000000007
#define ll long long
using namespace std;
ll fact[maxn];
ll n,m;
ll prime[maxm],book[maxm];
void Euler()
{
	for(ll i=2;i<maxm;i++)
	{
		if(!book[i]) prime[++prime[0]]=i;
		for(ll j=1;j<=prime[0]&&i*prime[j]<maxm;j++)
		{
			book[i*prime[j]]=1;
			if(i%prime[j]==0) break;
		}
	}
}
ll ksm(ll a,ll b){ll s=1;while(b){if(b&1) s=s*a%p; a=a*a%p; b>>=1;}return s;}
ll C(ll n,ll m)
{
	if(n<m) return 0;
	return (fact[n]*ksm(fact[n-m],p-2))%p*ksm(fact[m],p-2)%p;
}
void solve()
{
	ll n,m;
	ll ans=1;
	scanf("%lld%lld",&n,&m);
	for(ll i=1;prime[i]<=m;i++)
	{
		if(m%prime[i]==0)
		{
			ll cnt=0;
			while(m%prime[i]==0) m/=prime[i],cnt++;
			ans=ans*C(cnt+n-1,n-1)%p;
		}
	}
	printf("%lld\n",ans);
	ans=0;			
}
int main()
{
	Euler();
	fact[0]=1;
	for(ll i=1;i<maxn;i++) fact[i]=fact[i-1]*i%p;
	solve();
	return 0;
}