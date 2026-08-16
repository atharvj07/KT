#include <cstdio>
#include <algorithm>
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define rep(i, n) REP(i, 0, n)
#define INF (1<<29)
using namespace std;
int C[2][100][100];
int main()
{
	while (true) {
		int n, m; scanf("%d %d", &n, &m);
		if (n == 0 && m == 0) break;
		rep(k, 2) rep(i, 100) {
			rep(j, 100) { C[k][i][j] = INF; }
			C[k][i][i] = 0;
		}
		rep(i, n) {
			int a, b, c, t; scanf("%d%d%d%d", &a, &b, &c, &t);
			a--, b--;
			C[0][a][b] = C[0][b][a] = c;
			C[1][a][b] = C[1][b][a] = t;
		}
		rep(k, m) rep(i, m) rep(j, m) rep(l, 2) {
			C[l][i][j] = min(C[l][i][k] + C[l][k][j], C[l][i][j]);
		}
		int k; scanf("%d", &k);
		rep(i, k) {
			int p, q, r; scanf("%d%d%d", &p, &q, &r);
			printf("%d\n", C[r][p-1][q-1]);
		}
	}
	return 0;
}