#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define FOR(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define FORR(i,a,b) for(int i=(int)(b)-1;i>=(int)(a);i--)

#define CHMIN(a,b) (a)=min((a),(b))
#define CHMAX(a,b) (a)=max((a),(b))

#define DEBUG(x) cout<<#x<<": "<<(x)<<endl

#define MOD 998244353

int n,k;
vi g[125252];

pair<vi,vi> dfs(int p, int bef){
	vi v0({1});
	vi v1({0,1});
	for(int to : g[p])if(to != bef){
		pair<vi,vi> PVV = dfs(to,p);
		vi w0 = PVV.first;
		vi w1 = PVV.second;
		vi nv0(min(k+1,(int)(v0.size() + max(w0.size(), w1.size()) - 1)));
		vi nv1(min(k+1,(int)(v1.size() + max(w0.size(), w1.size()) - 1)));
		REP(i,v0.size())REP(j,w0.size()){
			if(i+j<nv0.size()){
				(nv0[i+j] += 1ll*v0[i]*w0[j]%MOD) %= MOD;
			}
		}
		REP(i,v0.size())REP(j,w1.size()){
			if(i+j<nv0.size()){
				(nv0[i+j] += 1ll*v0[i]*w1[j]%MOD) %= MOD;
			}
		}
		REP(i,v1.size())REP(j,w0.size()){
			if(i+j<nv1.size()){
				(nv1[i+j] += 1ll*v1[i]*w0[j]%MOD) %= MOD;
			}
		}
		REP(i,v1.size())REP(j,w1.size()){
			if(i+j<nv1.size()){
				(nv1[i+j] += 1ll*v1[i]*w1[j]%MOD) %= MOD;
			}
			if(i+j-1>=0 && i+j-1<nv1.size()){
				(nv1[i+j-1] += 1ll*v1[i]*w1[j]%MOD) %= MOD;
			}
		}
		v0 = nv0;
		v1 = nv1;
	}
	return make_pair(v0,v1);
}

int main(){
	scanf("%d%d",&n,&k);
	REP(i,n-1){
		int a,b;
		scanf("%d%d",&a,&b);
		--a; --b;
		g[a].push_back(b);
		g[b].push_back(a);
	}
	pair<vi,vi> ans = dfs(0,-1);
	int sum = 0;
	if(ans.first.size() > k)sum += ans.first[k];
	if(ans.second.size() > k)sum += ans.second[k];
	printf("%d\n",sum%MOD);
	return 0;
}
