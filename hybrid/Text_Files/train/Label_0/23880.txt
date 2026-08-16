#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for(ll (i) = (0);(i) < (n);++i)
#define REV(i,n) for(ll (i) = (n) - 1;(i) >= 0;--i)
#define PB push_back
#define EB emplace_back
#define MP make_pair
#define FI first
#define SE second
#define SHOW1d(v,n) {REP(WW,n)cerr << v[WW] << ' ';cerr << endl << endl;}
#define SHOW2d(v,WW,HH) {REP(W_,WW){REP(H_,HH)cerr << v[W_][H_] << ' ';cerr << endl;}cerr << endl;}
#define ALL(v) v.begin(),v.end()
#define Decimal fixed<<setprecision(20)
#define INF 1000000000
#define LLINF 1000000000000000000LL
#define MOD 998244353

typedef long long ll;
typedef pair<ll,ll> P;

ll ans = LLINF;

ll dp[2][11111];

void init(){
	REP(i, 2)REP(j, 11111)dp[i][j] = -LLINF;
	REP(i, 2)dp[i][0] = LLINF;
}

void check(ll c_max, int a, int b, int w){
	deque<P> deq;
	ll r = 1;
	for(ll i = 1;i <= w;i++){
		while(r < i)r++;
		while(r <= w && (c_max - dp[b][r] > r - i)){
			while(!deq.empty() && deq.back().FI < dp[b][r]){
				deq.pop_back();
			}
			if(dp[b][r] != -LLINF)deq.push_back(MP(dp[b][r], r));
			r++;
		}
		while(!deq.empty() && deq.front().SE < i)deq.pop_front();

		if(dp[a][i] == -LLINF)continue;
		if(!deq.empty()) {
			ans = min(ans, c_max - min(dp[a][i], deq.front().FI));
		}
		if(r <= w && dp[b][r] != -INF){
			ans = min(ans, max(r - i, c_max - dp[a][i]));
		}
	}
}

void query(P cat, ll type, ll w){
	REV(i, 11111){
		if(i + cat.SE >= 11111)continue;
		if(dp[type][i] == -LLINF)continue;

		dp[type][i + cat.SE] = max(dp[type][i + cat.SE], min(dp[type][i], cat.FI));
	}

	check(cat.FI, 0, 1, w);
	check(cat.FI, 1, 0, w);
}

int main(){
	cin.tie(0);cout.tie(0);ios::sync_with_stdio(false);

	init();

	ll na, nb, w;cin >> na >> nb >> w;
	vector<pair<P, ll>> v;

	REP(i, na){
		ll m, c;cin >> m >> c;
		v.EB(MP(c, m), 0);
	}
	REP(i, nb){
		ll m, c;cin >> m >> c;
		v.EB(MP(c, m), 1);
	}

	sort(ALL(v));
	REP(i, v.size()){
		query(v[i].FI, v[i].SE, w);
	}

	cout << ans << endl;

	return 0;
}

