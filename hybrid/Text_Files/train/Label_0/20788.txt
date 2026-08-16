#include<cmath>
#include<cstdio>
#include<vector>
#include<cstring>
#include<algorithm>

#define rep(i,n) for(ll i=0;i<(n);i++)

using namespace std;

typedef long long ll;

const ll INF=1<<29;

ll knapsack(const vector<ll> &w,const vector<ll> &p,ll W){
	ll dp[10001];
	rep(j,W+1) dp[j]=(j==0?0:-INF);
	rep(i,w.size()) rep(j,W-w[i]+1) dp[j+w[i]]=max(dp[j+w[i]],dp[j]+p[i]);
	return *max_element(dp,dp+W+1);
}

ll TSP(ll n,const ll d0[7],const ll d[7][7],ll S_tar){
	if(S_tar==0) return 0;

	ll dp[1<<7][7];
	rep(S,1<<n) rep(i,n) dp[S][i]=INF;
	rep(i,n) dp[1<<i][i]=d0[i];
	rep(S,1<<n) rep(i,n) if(S&1<<i) {
		rep(j,n) if(!(S&1<<j)) dp[S|1<<j][j]=min(dp[S|1<<j][j],dp[S][i]+d[i][j]);
	}
	ll res=INF;
	rep(i,n) res=min(res,dp[S_tar][i]+d0[i]);
	return res;
}

int main(){
	ll n,m,W,T; scanf("%lld%lld%lld%lld",&n,&m,&W,&T);
	char s_sell[7][8];
	ll weight[7],sell[7];
	rep(i,m) scanf("%s%lld%lld",s_sell[i],weight+i,sell+i);

	ll num[7],x[7],y[7];
	char s_buy[7][7][8];
	ll buy[7][7];
	rep(i,n){
		scanf("%lld%lld%lld",num+i,x+i,y+i);
		rep(j,num[i]) scanf("%s%lld",s_buy[i][j],buy[i]+j);
	}

	ll value[1<<7]; // value[S] := ( 町の集合 S を回るとき, 重さ<=W となる価値の総和の最大値 )
	rep(S,1<<n){
		vector<ll> w,p;
		rep(i,n) if(S&1<<i) rep(j,num[i]) {
			ll k;
			for(k=0;strcmp(s_sell[k],s_buy[i][j])!=0;k++);
			if(sell[k]>buy[i][j]){
				w.push_back(weight[k]);
				p.push_back(sell[k]-buy[i][j]);
			}
		}
		value[S]=knapsack(w,p,W);
	}

	ll d0[7]; // 市場との距離
	rep(i,n) d0[i]=abs(x[i])+abs(y[i]);
	ll d[7][7]; // 町と町との距離
	rep(i,n) rep(j,n) d[i][j]=abs(x[i]-x[j])+abs(y[i]-y[j]);

	ll dist[1<<7]; // dist[S] := ( 市場からスタートして, 町の集合 S をすべて回って市場に戻ってくる最短距離 )
	rep(S,1<<n) dist[S]=TSP(n,d0,d,S);

	// 今度は距離をコストだと思って, 品物の数 2^n の非有界ナップザック問題を解く
	vector<ll> w,p;
	rep(S,1<<n){
		w.push_back(dist[S]);
		p.push_back(value[S]);
	}
	printf("%lld\n",knapsack(w,p,T));

	return 0;
}