#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
using namespace std;

typedef long long LL;
typedef pair<int,int> pii;

const LL MOD = 1000000007;

const int DEG = 2100;
const int BASE = 4100;

void add(LL &x, LL y){
	x += y;
	if(x >= MOD){ x -= MOD; }
}

LL powmod(LL x, LL y){
	LL a = 1;
	while(y){
		if(y & 1){ a = a * x % MOD; }
		x = x * x % MOD;
		y >>= 1;
	}
	return a;
}

LL invs[DEG + 1];

void solve(int n, int m){
	vector<vector<pii>> G(n);
	for(int i = 0; i < m; ++i){
		int s, t, d;
		cin >> s >> t >> d;
		G[s - 1].emplace_back(t - 1, d);
	}

	vector<vector<LL>> cnts(n, vector<LL>(BASE + DEG + 1));
	cnts[0][0] = 1;
	for(int u = 0; u < n; ++u){
		auto &from = cnts[u];
		for(int i = 0; i < BASE + DEG; ++i){
			add(from[i + 1], from[i]);
		}
		for(const auto &p : G[u]){
			auto &to = cnts[p.first];
			for(int i = 0; i + p.second <= BASE + DEG; ++i){
				add(to[i + p.second], from[i]);
			}
		}
	}

	vector<LL> ltmul(DEG + 2), rtmul(DEG + 2);
	int q;
	cin >> q;
	for(int qnum = 0; qnum < q; ++qnum){
		int e;
		LL t;
		cin >> e >> t;
		--e;

		LL res = 0;
		if(t <= BASE + DEG){
			res = cnts[e][t];
		}
		else{
			LL s = (t - BASE) % MOD;
			ltmul[0] = 1;
			for(int i = 0; i <= DEG; ++i){
				ltmul[i + 1] = ltmul[i] * (s - i) % MOD;
			}
			rtmul.back() = 1;
			for(int i = DEG; i >= 0; --i){
				rtmul[i] = rtmul[i + 1] * (s - i) % MOD;
			}
			for(int i = 0; i <= DEG; ++i){
				LL x = ltmul[i] * rtmul[i + 1] % MOD * invs[i] % MOD;
				res = (res + x * cnts[e][i + BASE]) % MOD;
			}
		}
		
		res = (res % MOD + MOD) % MOD;
		cout << res << '\n';
	}
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);

	LL f = 1;
	for(int i = 1; i <= DEG; ++i){
		f = f * -i % MOD;
	}
	for(int i = 0; i <= DEG; ++i){
		invs[i] = powmod(f, MOD - 2);
		f = f * (i + 1) % MOD;
		f = f * powmod(i - DEG, MOD - 2) % MOD;
	}

	int n, m;
	while(cin >> n >> m && n){
		solve(n, m);
	}
}

