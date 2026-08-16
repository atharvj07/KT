#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define mp make_pair
#define pb push_back

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define rep(i, n) for (int i = 0; i < (int)(n); ++ i)

#define ull unsigned long long

const int mxn = 505;
int n, s[mxn], t[mxn];
ull u[mxn], v[mxn], x[mxn][mxn];
int nw[mxn][mxn];
int vx[mxn], xsz, vy[mxn], ysz;

bool chk() {
	rep(i, n) if (s[i] == 0) { ull c = (ull)(-1); rep(j, n) c &= x[i][j]; if (c != u[i]) return 0; }
	rep(j, n) if (t[j] == 0) { ull c = (ull)(-1); rep(i, n) c &= x[i][j]; if (c != v[j]) return 0; }
	rep(i, n) if (s[i] == 1) { ull c = 0; rep(j, n) c |= x[i][j]; if (c != u[i]) return 0; }
	rep(j, n) if (t[j] == 1) { ull c = 0; rep(i, n) c |= x[i][j]; if (c != v[j]) return 0; }
	return 1;
}

int main() {
	scanf("%d", &n);
	rep(i, n) scanf("%d", &s[i]);
	rep(i, n) scanf("%d", &t[i]);
	rep(i, n) scanf("%llu", &u[i]);
	rep(i, n) scanf("%llu", &v[i]);
	rep(lv, 64) {
		xsz = ysz = 0;
		rep(i, n) {
			if (s[i] == 0 && (u[i] >> lv & 1) == 1) rep(j, n) nw[i][j] = 1; else
			if (s[i] == 1 && (u[i] >> lv & 1) == 0) rep(j, n) nw[i][j] = 0; else
			vx[xsz ++] = i;
		}
		rep(j, n) {
			if (t[j] == 0 && (v[j] >> lv & 1) == 1) rep(i, n) nw[i][j] = 1; else
			if (t[j] == 1 && (v[j] >> lv & 1) == 0) rep(i, n) nw[i][j] = 0; else
			vy[ysz ++] = j;
		}
		if (xsz == 0 || ysz == 0) {
		} else if (xsz == 1) {
			rep(j, ysz) {
				bool ok = 0;
				rep(i, n) if (i != vx[0] && nw[i][vy[j]] == (v[vy[j]] >> lv & 1)) { ok = 1; break; }
				if (ok) nw[vx[0]][vy[j]] = u[vx[0]] >> lv & 1; else nw[vx[0]][vy[j]] = v[vy[j]] >> lv & 1;
			}
		} else if (ysz == 1) {
			rep(i, xsz) {
				bool ok = 0;
				rep(j, n) if (j != vy[0] && nw[vx[i]][j] == (u[vx[i]] >> lv & 1)) { ok = 1; break; }
				if (ok) nw[vx[i]][vy[0]] = v[vy[0]] >> lv & 1; else nw[vx[i]][vy[0]] = u[vx[i]] >> lv & 1;
			}
		} else {
			rep(i, xsz) rep(j, ysz) nw[vx[i]][vy[j]] = (i + j) & 1;
		}
		rep(i, n) rep(j, n) x[i][j] |= (ull)(nw[i][j]) << lv;
	}
	if (!chk()) { puts("-1"); return 0; }
	rep(i, n) rep(j, n) printf("%llu%c", x[i][j], " \n"[j + 1 == n]);
	return 0;
}
