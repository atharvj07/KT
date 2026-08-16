#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sqr(x) ((x)*(x))
#define mp make_pair
#define ld long double
#define PI pair<int,int>
inline char gc(){
    static char buf[100000],*p1=buf,*p2=buf;
    return p1==p2&&(p2=(p1=buf)+fread(buf,1,100000,stdin),p1==p2)?EOF:*p1++;
}
#define gc getchar
inline ll read(){
	ll x = 0; char ch = gc(); bool positive = 1;
	for (; !isdigit(ch); ch = gc())	if (ch == '-')	positive = 0;
	for (; isdigit(ch); ch = gc())	x = x * 10 + ch - '0';
	return positive ? x : -x;
}
inline void write(ll a){
    if(a<0){
    	a=-a; putchar('-');
	}
    if(a>=10)write(a/10);
    putchar('0'+a%10);
}
inline void writeln(ll a){write(a); puts("");}
inline void wri(ll a){write(a); putchar(' ');}
const int N=200005;
int a[N],q[N],top,A[N];
ll f[N],g[N];
int cmp(ll a,ll b,int c){
	if(a>b){
		while(a>b){b<<=2; c+=2;}
		return c;
	}else{
		while(a<=b){a<<=2; c-=2;}
		return c+2;
	}
}
int main(){
	int n=read();
	for(int i=1;i<=n;i++)a[i]=read(); q[0]=n+1;
	ll dq=0;
	for(int i=n;i;i--){
		int t=0;
		while(top){
			int jb=cmp(a[q[top]-1],a[q[top]],t);
			if(jb>0){
				dq+=(ll)jb*(q[top-1]-q[top]); t=jb+A[top]; top--;
			}else break;
		}
		q[++top]=i; 
		A[top]=t;
		f[i]=dq;
	}
	dq=top=q[0]=0;
	for(int i=1;i<=n;i++){
		int t=0;
		a[i]*=2;
		while(top){
			int jb=cmp(a[q[top]+1],a[q[top]],t);
			if(jb>0){
				dq+=(ll)jb*(q[top]-q[top-1]); t=jb+A[top]; top--;
			}else break;
		}
		q[++top]=i; 
		A[top]=t;
		g[i]=dq;
		//cout<<g[i]<<" fjzzq "<<f[i]<<endl;
	}
	ll ans=1e18;
	for(int i=0;i<=n;i++){
		ans=min(ans,g[i]+f[i+1]+i);
	}
	cout<<ans<<endl;
}
