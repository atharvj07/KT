#include<bits/stdc++.h>
using namespace std;
int n,m,p,k,q,dp[64][2][3];
long long x[10010],y[10010];//dep,lim,mod
bool light(long long xx,long long yy){
	bool flag=0;
	for(int i=1;i<=n;i++){
		if(yy-y[i]<0||yy-y[i]>x[i]-xx) continue;
		flag^=(((x[i]-xx)|(yy-y[i]))==x[i]-xx);
	}
	return flag;
}
bool lres[3],rres[3],mres[3],res[3];
void calc(long long c,long long xx,long long yy,long long r){
	long long tmp=xx-c;r-=yy;
	if(r<0) return res[0]=res[1]=res[2]=0,void();
	memset(dp,0,sizeof(dp));
	dp[63][1][0]=1;
	for(int i=63;i>=1;i--){
		if(!((tmp>>(i-1))&1)){
			for(int j=0;j<3;j++){
				if(dp[i][0][j]) dp[i-1][0][(j*2)%3]^=1;
				if(dp[i][1][j]){
					if((r>>(i-1))&1) dp[i-1][0][(j*2)%3]^=1;
					else dp[i-1][1][(j*2)%3]^=1;
				}
			}
		}
		else{
			for(int j=0;j<3;j++){
				if(dp[i][0][j]) dp[i-1][0][(j*2)%3]^=1,dp[i-1][0][(j*2+1)%3]^=1;
				if(dp[i][1][j]){
					if((r>>(i-1))&1) dp[i-1][0][(j*2)%3]^=1,dp[i-1][1][(j*2+1)%3]^=1;
					else dp[i-1][1][(j*2)%3]^=1;
				}
			}
		}
	}
	yy=(yy%3+3)%3;
	res[yy]=dp[0][0][0]^dp[0][1][0];
	res[(yy+1)%3]=dp[0][0][1]^dp[0][1][1];
	res[(yy+2)%3]=dp[0][0][2]^dp[0][1][2];
}
long long work(long long c){
	long long l=-1e18,r=1e18,mid;
	for(int i=1;i<=n;i++){
		calc(c,x[i],y[i],r);
		rres[0]^=res[0],rres[1]^=res[1],rres[2]^=res[2];
	}
	int pos=0;
	for(int i=0;i<3;i++) if(rres[i]){
		pos=i;
		break;
	}
	while(l<r){
		mid=(l+r)>>1;memset(mres,0,sizeof(mres));
		for(int i=1;i<=n;i++){
			calc(c,x[i],y[i],mid);
			mres[0]^=res[0],mres[1]^=res[1],mres[2]^=res[2];
		}
		if(mres[pos]!=lres[pos]){
			r=mid;
			for(int i=0;i<3;i++) rres[i]=mres[i];
		}
		else{
			l=mid+1;
			for(int i=0;i<3;i++) lres[i]=mres[i];
		}
	}
	return l;
}
int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++) scanf("%lld%lld",&x[i],&y[i]);
	long long k=work(-1e17),lk=k,rk=k;
	for(int i=62;i>=0;i--) if(light(-1e17,lk-(1ll<<i))) lk-=1ll<<i;
	for(int i=62;i>=0;i--) if(light(-1e17,rk+(1ll<<i))) rk+=1ll<<i;
	printf("%lld %lld\n",(long long)(-1e17)+rk-lk,lk);
}
