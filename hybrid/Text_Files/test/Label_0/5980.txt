#include<iostream>
#include<vector>
#include<algorithm>
#include<iomanip>
#include<sstream>
#include<map>
#include<queue>
using namespace std;
#define int long long
vector<vector<int> >g;
vector<int> v;
void dfs(int a) {
	v[a] = 1;
	for (int i = 0; i < g[a].size(); i++) {
		if (v[g[a][i]] == 0) {
			dfs(g[a][i]);
		}
	}
}
signed main() {
	int N;
	int M;
	cin >> N >> M;
	g.resize(N);
	v.resize(N, 0);
	vector<int> W(N);
	for (int i = 0; i < N; i++) {
		cin >> W[i];
	}
	int a, b;
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		a--;
		b--;
		g[a].push_back(b);
		g[b].push_back(a);
	}
	dfs(0);
	vector<int> deg(N);
	int INF = (int)1 << 60;
	vector<int> dp(N, 0);
	for (int i = 0; i < N; i++) {
		deg[i] = g[i].size();
	}
	queue<int> qu;
	for (int i = 1; i < N; i++) {
		if (v[i] == 1) {
			if (deg[i] == 1) {
				qu.push(i);
				dp[i] = 0;
			}
		}
	}
	while (!qu.empty()) {
		int a = qu.front(); qu.pop();
		for (int i = 0; i < g[a].size(); i++) {

			deg[g[a][i]]--;
			if (g[a][i] != 0) {
				if (deg[g[a][i]] == 1) {
					qu.push(g[a][i]);
				}
			}
			dp[g[a][i]] = max(dp[g[a][i]], dp[a] + W[a]);
		}
	}

	int mx = 0;
	int res = 0;
	res = W[0];
	mx = dp[0];
	for (int i = 1; i < N; i++) {
		if (v[i] == 1) {
			if (deg[i] >= 2) {
				res += W[i];
				mx = max(mx, dp[i]);
			}
		}
	}
	res += mx;
	cout << res << endl;
}
