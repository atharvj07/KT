#include <bits/stdc++.h>
using namespace std;
const int N = 50;
struct point {
	int x, y;
	point() {}
	point(int x, int y) : x(x), y(y) {}
};
int dot(const point &a, const point &b) { return a.x * b.x + a.y * b.y; }
int det(const point &a, const point &b) { return a.x * b.y - a.y * b.x; }
point operator + (const point &a, const point &b) { return point(a.x + b.x, a.y + b.y); }
point operator - (const point &a, const point &b) { return point(a.x - b.x, a.y - b.y); }
bool operator == (const point &a, const point &b) { return a.x == b.x && a.y == b.y; }
struct line {
	point s, t;
	line() {}
	line(point a, point b) : s(a), t(b) {}
};
int sign(int x) {
	return (x > 0) - (x < 0);
}
bool on(line a, point b) {
	return sign(dot(b - a.s, a.t - a.s)) * sign(dot(b - a.t, a.t - a.s)) <= 0;
}
bool judge(line a, line b) {
	//printf("judge %d %d -> %d %d    %d %d -> %d %d\n", a.s.x, a.s.y, a.t.x, a.t.y, b.s.x, b.s.y, b.t.x, b.t.y);
	if (a.s == a.t || b.s == b.t) return 0;
	if (det(a.t - a.s, b.t - b.s) || det(a.t - b.s, b.t - b.s) || det(a.s - b.s, b.t - b.s)) return 0;
	int d = dot(a.t - a.s, a.t - a.s);
	int L = dot(a.t - a.s, b.s - a.s);
	int R = dot(a.t - a.s, b.t - a.s);
	if (L > R) swap(L, R);
	//printf("%d - %d   %d - %d\n", 0, d, L, R);
	L = max(0, L);
	R = min(d, R);
	return L < R;
}
vector<int> G[N];
vector<point> poly[N];
int cnt[N], id[N], col[N];
bool adj[N][N], vis[N];
int ban[N][3], cho[N];
bool cmp(int i, int j) { return cnt[i] > cnt[j]; }
vector<int> lis;
bool is_bit;
void dfs(int x, int col = 0) {
	if (vis[x]) {
		is_bit &= (col == ::col[x]);
		return;
	}
	vis[x] = 1;
	::col[x] = col;
	for (int i = 0; i < (int) G[x].size(); ++ i) {
		int u = G[x][i];
		dfs(u, col ^ 1);
	}
	lis.push_back(x);
}
bool is_three;
int should;
bool inq[N];
int getnxt() {
	for (int i = 0; i < should; ++ i) {
		int x = lis[i];
		if (!inq[x] && cho[x] == 1) return x;
	}
	for (int i = 0; i < should; ++ i) {
		int x = lis[i];
		if (!inq[x]) return x;
	}
	assert(-1);
}
void dfs2(int id) {
	if (id == should) {
		is_three = 1;
		return;
	}
	int x = getnxt();
	inq[x] = 1;
	for (int c = 0; c < 3; ++ c) {
		if (ban[x][c]) continue;
		bool gg = 0;
		for (int i = 0; i < (int) G[x].size(); ++ i) {
			int u = G[x][i];
			if (inq[u]) continue;
			ban[u][c] ++;
			cho[u] -= (ban[u][c] == 1);
			if (cho[u] == 0) gg = 1;
		}
		if (!gg) dfs2(id + 1);
		if (is_three) return;
		for (int i = 0; i < (int) G[x].size(); ++ i) {
			int u = G[x][i];
			if (inq[u]) continue;
			ban[u][c] --;
			cho[u] += (ban[u][c] == 0);
		}
	}
	inq[x] = 0;
}
int work(int r) {
	lis.clear();
	is_bit = 1;
	dfs(r);
	if ((int) lis.size() == 1) return 1;
	if (is_bit) return 2;
	for (int i = 0; i < (int) lis.size(); ++ i) {
		int u = lis[i];
		cho[u] = 3;
		ban[u][0] = ban[u][1] = ban[u][2] = 0;
		inq[u] = 0;
	}
	is_three = 0;
	should = lis.size();
	sort(lis.begin(), lis.end(), cmp);
	dfs2(0);
	if (is_three) return 3;
	return 4;
}
int main() {
	int n;
	while (scanf("%d", &n) == 1 && n) {
		for (int i = 0; i < n; ++ i) {
			int m;
			scanf("%d", &m);
			poly[i].clear();
			for (int j = 0; j < m; ++ j) {
				int x, y;
				scanf("%d%d", &x, &y);
				poly[i].push_back(point(x, y));
			}
			poly[i].push_back(poly[i][0]);
		}
		for (int i = 0; i < n; ++ i) {
			cnt[i] = 0;
			G[i].clear();
			for (int j = 0; j < n; ++ j) adj[i][j] = 0;
			vis[i] = 0;
			id[i] = i;
		}
		//printf("n = %d\n", n);
		for (int i = 0; i < n; ++ i) {
			for (int j = i + 1; j < n; ++ j) {
				bool touch = 0;
				for (int k = 0; !touch && k < (int) poly[i].size() - 1; ++ k) {
					line a = line(poly[i][k], poly[i][k + 1]);
					for (int l = 0; !touch && l < (int) poly[j].size() - 1; ++ l) {
						line b = line(poly[j][l], poly[j][l + 1]);
						if (judge(a, b)) {
							touch = 1;
						}
					}
				}
				if (touch) {
					//printf("%d %d\n", i, j);
					G[i].push_back(j);
					G[j].push_back(i);
					adj[i][j] = adj[j][i] = 1;
					cnt[i] ++;
					cnt[j] ++;
				}
			}
		}
		sort(id, id + n, cmp);
		int ans = 0;
		for (int ii = 0; ii < n; ++ ii) {
			int i = id[ii];
			if (vis[i]) continue;
			ans = max(ans, work(i));
		}
		printf("%d\n", ans);
	}
}