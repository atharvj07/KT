#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <typeinfo>
#include <numeric>
#include <functional>
#include <unordered_map>
#include <bitset>
#include <stack>


using namespace std;
using ll = long long;
using ull = unsigned long long;

const ll INF = 1e16;
const ll MOD = 1e9 + 7;

#define REP(i, n) for(ll i = 0; i < n; i++)







int main() {
	ll n, m, k;
	cin >> n >> m >> k;
	vector<ll> dark(n, -1);
	vector<ll> d(m);
	REP(i, m) {
		cin >> d[i];
		d[i]--;
		dark[d[i]] = i;
	}
	vector<vector<ll>> v(n, vector<ll>(k));
	REP(i, n) {
		REP(j, k) {
			cin >> v[i][j];
			v[i][j]--;
		}
	}

	vector<bool> used(1 << m);
	queue<pair<ll, ll>> que;
	que.push({ (1 << m) - 1, 0 });
	while (!que.empty()) {
		auto tmp = que.front(); que.pop();
		ll now = tmp.first, cnt = tmp.second;
		if (used[now]) continue;
		used[now] = true;
		if (now == 0) {
			cout << cnt << endl;
			return 0;
		}
		REP(j, k) {
			ll next = 0;
			REP(i, m) {
				if (now & (1 << i) && dark[v[d[i]][j]] >= 0) {
					next |= 1 << dark[v[d[i]][j]];
				}
			}
			que.push({ next, cnt + 1 });
		}
	}
}
