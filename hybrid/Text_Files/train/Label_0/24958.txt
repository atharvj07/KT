#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		vector<vector<int>> G(n, vector<int>());
		for (int i = 0; i < n; ++i) {
			int u, v;
			cin >> u >> v;
			u--;
			v--;
			G[u].push_back(v);
			G[v].push_back(u);
		}

		vector<ll> cnt(n, 1);
		queue<int> Q;
		for (int i = 0; i < n; ++i)
			if (G[i].size() == 1)
				Q.push(i);

		while (!Q.empty()) {
			int u = Q.front();
			Q.pop();
			int p = G[u][0];
			cnt[p] += cnt[u];
			cnt[u] = 0;
			G[u].clear();
			G[p].erase(find(G[p].begin(), G[p].end(), u));
			if (G[p].size() == 1)
				Q.push(p);
		}

		ll ans = 0;
		for (int i = 0; i < n; ++i) {
			ans += 1LL * (cnt[i]) * (cnt[i] - 1) / 2;
			ans += 1LL * (cnt[i]) * (n - cnt[i]);
		}
		cout << ans << '\n';
	}
}
