#include<bits/stdc++.h>
#define int long long
#define fr(i,a,b) for(int i(a),end##i(b);i<=end##i;i++)
#define fd(i,a,b) for(int i(a),end##i(b);i>=end##i;i--)
using namespace std;
const int mod=998244353;
const int maxn=4e7+5;
int ksm(int x,int k){
	int ans=1;
	while(k){
		if(k&1)ans=ans*x%mod;
		x=x*x%mod;
		k>>=1;
	}
	return ans;
}
int jc[maxn],inv[maxn];
void init(int n){
	jc[0]=1;
	fr(i,1,n)jc[i]=jc[i-1]*i%mod;
	inv[n]=ksm(jc[n],mod-2);
	fd(i,n-1,0)inv[i]=inv[i+1]*(i+1)%mod;
}
int C(int n,int m){
	if(n<0||m<0||n<m)return 0;
	return jc[n]*inv[m]%mod*inv[n-m]%mod;
}
int D(int n,int m){
	if(n<0||n+m<0||((n+m)&1))return 0;
	return C(n,n+m>>1);	
}
int x,y,t,ans;
signed main(){
#ifdef pig
	freopen("f.in","r",stdin);
	freopen("f.out","w",stdout);
#endif
	cin>>t>>y>>x;
	if(!x&&!y&&t){
		cout<<1;
		return 0;
	}
	init(3e7);y=x-y;
	if(2*x-t-y==0)ans=D(t-1,2*x-t-1)-D(t-1,2*x-t+1);
	fr(k,1,2*x-y){	
		int h=2*x-k-y;
		(ans+=C(h+t-k-1,h)*(D(k-1,2*x-k-1)-D(k-1,2*x-k+1)))%=mod;	
	}
	cout<<(ans+mod)%mod;
	return 0;
}