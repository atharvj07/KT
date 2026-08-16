#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PII;
typedef double db;
mt19937 mrand(1); 
const ll mod=998244353;
int rnd(int x) { return mrand() % x;}
ll powmod(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}
// head

const int N=101000;
int p[N],n,a[N],rk[N];
void gao(string s,int t) {
	VI x,y;
	rep(i,0,n) if (s[i]=='1') {
		if (a[i]%2==0) x.pb(a[i]); else y.pb(a[i]);
	}
	if (t==1) x.swap(y);
	for (auto u:y) x.pb(u);
	int tt=0;
	rep(i,0,n) if (s[i]=='1') a[i]=x[tt++];
	
	/*rep(i,0,n) printf("%d ",a[i]);
	puts("");*/
	
	printf("%d %s\n",t,s.c_str());
}
int main() {
	scanf("%d",&n);
	int c=(n+1)/2;
	int even=0,odd=1;
	rep(i,0,n) {
		if (i<c) {
			if (i%2==0) p[i]=even,even+=2;
		} else {
			if (i%2==0) p[i]=odd,odd+=2;
		}
	}
	rep(i,0,n) {
		if (i<c) {
			if (i%2==1) p[i]=even,even+=2;
		} else {
			if (i%2==1) p[i]=odd,odd+=2;
		}
	}
	//rep(i,0,n) printf("%d ",p[i]);
	puts("29");
	rep(i,0,n) {
		if (p[i]%2==0) rk[p[i]]=i;
		else rk[p[i]]=n-i-1+(n%2);
		//printf("%d %d\n",p[i],rk[p[i]]);
	}
	rep(i,0,n) scanf("%d",a+i);
	//random_shuffle(a,a+n);
	rep(i,0,14) {
		gao(string(n,'1'),0);
		string s(n,'0');
		rep(j,0,n) {
			if (a[j]%2==0&&(rk[a[j]]&(1<<i))!=0) s[j]='1';
			if (a[j]%2==1&&(rk[a[j]]&(1<<i))!=0) s[j]='1';
		}
		gao(s,1);
	}
	string s(n,'0');
	rep(i,0,n) if (p[i]!=i) s[i]='1';
	gao(s,1);
}
