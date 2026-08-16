#include <bits/stdc++.h>
#define rep(i,n)for(int i=0;i<n;i++)
using namespace std;
typedef long long ll;
typedef pair<char, int>P;

int d1[100][100];
int d2[100][100];

int main() {
	int n, m;
	while (scanf("%d%d", &n, &m), n) {
		memset(d1, 0x3f, sizeof(d1));
		memset(d2, 0x3f, sizeof(d2));
		rep(i, n) {
			int a, b, cost, time;
			scanf("%d%d%d%d", &a, &b, &cost, &time);
			a--; b--;
			d1[a][b] = d1[b][a] = cost;
			d2[a][b] = d2[b][a] = time;
		}
		rep(k, m)rep(i, m)rep(j, m) {
			d1[i][j] = min(d1[i][j], d1[i][k] + d1[k][j]);
			d2[i][j] = min(d2[i][j], d2[i][k] + d2[k][j]);
		}
		int k; scanf("%d", &k);
		rep(i, k) {
			int p, q, r;
			scanf("%d%d%d", &p, &q, &r);
			p--; q--;
			if (r)printf("%d\n", d2[p][q]);
			else printf("%d\n", d1[p][q]);
		}
	}
	return 0;
}