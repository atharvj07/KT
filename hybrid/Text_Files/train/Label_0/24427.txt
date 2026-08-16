#ifdef xay5421
#define D(...) fprintf(stderr,__VA_ARGS__)
#else
#define D(...) ((void)0)
#define NDEBUG
#endif
#include<bits/stdc++.h>
#define int long long
#define LL long long
#define MP make_pair
#define PB push_back
#define EB emplace_back
#define fi first
#define se second
#define ALL(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define rep(i,a,b) for(int i=(a);i<=(b);++i)
#define per(i,a,b) for(int i=(a);i>=(b);--i)
using namespace std;
typedef pair<int,int>PII;typedef vector<int>VI;typedef vector<PII>VII;
template<typename T>void rd(T&x){int f=0,c;while(!isdigit(c=getchar()))f^=!(c^45);x=(c&15);while(isdigit(c=getchar()))x=x*10+(c&15);if(f)x=-x;}
template<typename T>void pt(T x,int c=-1){if(x<0)putchar('-'),x=-x;if(x>9)pt(x/10);putchar(x%10+48);if(c!=-1)putchar(c);}
int x;
void exgcd(int a,int b,int&x,int&y){
	if(!b){
		x=1,y=0;
		return;
	}
	exgcd(b,a%b,y,x);
	y-=a/b*x;
}
signed main(){
	rd(x);
	x*=2;
	vector<pair<int,int> >d;
	rep(i,2,x/i)while(x%i==0){
		if(d.empty()||d.back().fi!=i){
			d.EB(i,i);
		}else{
			d.back().se*=i;
		}
		x/=i;
	}
	if(x>1){
		d.EB(x,x);
	}
	int ans=1e18;
	rep(i,0,(1<<SZ(d))-1){
		int d1=1,d2=1;
		rep(j,0,SZ(d)-1)
			if(i>>j&1){
				d1*=d[j].se;
			}else{
				d2*=d[j].se;
			}
		int k1,k2;
		exgcd(d1,d2,k1,k2);
		if(k1<0){
			int t=(-k1)/d2+1;
			k1+=t*d2,k2-=t*d1;
		}
		int t=min((k1-1)/d2,(-k2-1)/d1);
		k1-=t*d2,k2+=t*d1;
		assert(k1*d1+k2*d2==1);
		D("%lld %lld\n",k1,d1);
		if(k1>0&&k2<0)ans=min(ans,k1*d1-1);
	}
	pt(ans,'\n');
	return 0;
}
