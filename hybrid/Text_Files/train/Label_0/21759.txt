#include <bits/stdc++.h>
using namespace std;

const int N = 1505, mod = 1e9 + 9;

int n, m, a[N][N], b[N][N], A[N], id[N], d[N];

vector <int> ans;

bool vis[N];

queue <int> q;

int main() {
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; i++) 
		for (int j = 1; j <= m; j++)
			scanf("%d", &a[i][j]), A[i] = (A[i]*233ll + a[i][j])%mod;
	for (int i = 1; i <= n; i++) {
		int h = 0;
		for (int j = 1; j <= m; j++)
			scanf("%d", &b[i][j]), h = (h*233ll + b[i][j])%mod;
		for (int j = 1; j <= n; j++)
			if (!vis[j] && A[j] == h) {
				vis[j] = 1, id[i] = j;
				break;
			}
		if (!id[i])
			return puts("-1"), 0;
	}
	memset(vis, 0, sizeof(vis));
	for (int j = 1; j <= m; j++)
		for (int i = 1; i < n; i++)
			d[j] += b[i][j] > b[i + 1][j];
	for (int j = 1; j <= m; j++)
		if (!d[j])
			q.push(j);
	while (!q.empty()) {
		int u = q.front(); q.pop();
		ans.push_back(u);
		for (int i = 1; i < n; i++)
			if (b[i][u] < b[i + 1][u] && !vis[i]) {
				vis[i] = 1;
				for (int j = 1; j <= m; j++) 
					if (b[i][j] > b[i + 1][j]) {
						if (!--d[j])
							q.push(j);
					}
			}
	}
	for (int i = 1; i < n; i++)
		if (!vis[i] && id[i] > id[i + 1])
			return puts("-1"), 0;
	cout<<ans.size()<<'\n';
	for (int i = ans.size() - 1; i >= 0; i--)
		printf("%d ", ans[i]);
}
