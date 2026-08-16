
// Problem : E. Advertising Agency
// Contest : Codeforces - Codeforces Round #697 (Div. 3)
// URL : https://codeforces.com/contest/1475/problem/E
// Memory Limit : 256 MB
// Time Limit : 2000 ms
// Powered by CP Editor (https://github.com/cpeditor/cpeditor)

#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll power(ll x,ll y,ll m){if(y==0)return 1;ll p=power(x,y/2,m)%m;p=(p*p)%m;return (y%2==0)?p:(x*p)%m;}
ll nCr(ll n,ll r,ll m){if(r>n)return 0;ll a=1,b=1,i;for(i=0;i<r;i++){a=(a*n)%m;--n;}while(r){b=(b*r)%m;--r;}return (a*power(b,m-2,m))%m;}
vector<ll> fac;
ll nCr2(ll n,ll r,ll m){if(r>n) return 0;return (((fac[n]*power(fac[r],m-2,m))%m)*power(fac[n-r],m-2,m))%m;}
ll gcd(ll a, ll b) {return (b ? gcd(b, a % b) : a);}
#define Test int t;cin>>t;while(t--)
#define endl '\n'
const ll mod = (ll)1e9 + 7;
void solve()
{
	ll n,k;
	cin >> n >> k;
	vector<ll> v(n);
	for(int i=0;i<n;++i)
	{
		cin >> v[i];
	}
	sort(v.rbegin(),v.rend());
	ll mx=0,last=-1;
	for(int i=0;i<k;++i)
	{
		mx+=v[i];
		last=v[i];
	}
	ll cnt1=0;
	ll cnt2=0;
	for(int i=0;i<k;++i)
	{
		if(v[i]==last)
		{cnt1++;cnt2++;}
	}
	for(int i=k;i<n;++i)
	{
		if(v[i]==last)
		cnt2++;
	}
	cout << nCr2(cnt2,cnt1,mod) << endl;
}
int main()
{
	fac = vector<ll>(10000);
	fac[0]=1;
	for(ll i=1;i<10000;++i)
	{
		fac[i]=fac[i-1]*i;
		fac[i]%=mod;
	}
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	Test
	solve();
	return 0;
}
