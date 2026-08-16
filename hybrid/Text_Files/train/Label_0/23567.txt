#include <stdio.h>
#include <sys/time.h>

#define N	200000
#define N_	(1 << 18)	/* N_ = pow2(ceil(log2(N))) */
#define LG	17	/* LG = floor(log2(10^5)) + 1 */
#define INF	0x3f3f3f3f3f3f3f3f

long long min(long long a, long long b) { return a < b ? a : b; }

unsigned int X;

void srand_() {
	struct timeval tv;

	gettimeofday(&tv, NULL);
	X = tv.tv_sec ^ tv.tv_usec;
	if (X % 2 == 0)
		X++;
}

int rand_() {
	return (X *= 3) >> 1;
}

long long aa[N]; int vv[N], ww[N], ii[N], inv[N], n;

void sort(int *ii, int l, int r) {
	while (l < r) {
		int i = l, j = l, k = r, i_ = ii[l + rand_() % (r - l)], tmp;

		while (j < k) {
			int c = vv[ii[j]] != vv[i_] ? vv[i_] - vv[ii[j]] : ww[ii[j]] - ww[i_];

			if (c == 0)
				j++;
			else if (c < 0) {
				tmp = ii[i], ii[i] = ii[j], ii[j] = tmp;
				i++, j++;
			} else {
				k--;
				tmp = ii[j], ii[j] = ii[k], ii[k] = tmp;
			}
		}
		sort(ii, l, i);
		l = k;
	}
}

long long vsm[LG + 1][N_ * 2], wsm[LG + 1][N_ * 2], wsm_[LG + 1][N_ * 2]; int n_;

void pul(int lg, int i) {
	int l = i << 1, r = l | 1;

	vsm[lg][i] = vsm[lg][l] + vsm[lg][r], wsm[lg][i] = wsm[lg][l] + wsm[lg][r];
	wsm_[lg][i] = min(wsm_[lg][l], wsm[lg][l] + wsm_[lg][r]);
}

void build() {
	int lg, i;

	n_ = 1;
	while (n_ < n)
		n_ <<= 1;
	for (lg = 0; lg <= LG; lg++) {
		for (i = 0; i < n_; i++) {
			long long a = aa[ii[i]];
			int v = vv[ii[i]], w = ww[ii[i]];

			if (i >= n)
				vsm[lg][n_ + i] = 0, wsm[lg][n_ + i] = 0, wsm_[lg][n_ + i] = INF;
			else if (w < (1 << lg))
				vsm[lg][n_ + i] = a * v, wsm[lg][n_ + i] = a * w, wsm_[lg][n_ + i] = INF;
			else
				vsm[lg][n_ + i] = 0, wsm[lg][n_ + i] = 0, wsm_[lg][n_ + i] = a == 0 ? INF : w;
		}
		for (i = n_ - 1; i > 0; i--)
			pul(lg, i);
	}
}

void update(int lg, int i) {
	long long a = aa[ii[i]];
	int v = vv[ii[i]], w = ww[ii[i]];

	if (w < (1 << lg))
		vsm[lg][n_ + i] = a * v, wsm[lg][n_ + i] = a * w, wsm_[lg][n_ + i] = INF;
	else
		vsm[lg][n_ + i] = 0, wsm[lg][n_ + i] = 0, wsm_[lg][n_ + i] = a == 0 ? INF : w;
	i += n_;
	while (i > 1)
		pul(lg, i >>= 1);
}

void update_(int i, int a) {
	int lg;

	aa[ii[i]] += a;
	for (lg = 0; lg <= LG; lg++)
		update(lg, i);
}

long long c, ans;

int jump(int lg, int i) {
	int l = i, r = n_ - 1;

	for (l += n_, r += n_; l <= r; l >>= 1, r >>= 1)
		if ((l & 1) == 1) {
			if (c >= wsm_[lg][l]) {
				while (l < n_)
					if (c >= wsm_[lg][l << 1 | 0])
						l = l << 1 | 0;
					else
						c -= wsm[lg][l << 1 | 0], ans += vsm[lg][l << 1 | 0], l = l << 1 | 1;
				l -= n_;
				c -= ww[ii[l]], ans += vv[ii[l]];
				return l + 1;
			} else if (c >= wsm[lg][l])
				c -= wsm[lg][l], ans += vsm[lg][l], l++;
			else {
				while (l < n_)
					if (c < wsm[lg][l << 1 | 0])
						l = l << 1 | 0;
					else
						c -= wsm[lg][l << 1 | 0], ans += vsm[lg][l << 1 | 0], l = l << 1 | 1;
				l -= n_;
				ans += c / ww[ii[l]] * vv[ii[l]], c %= ww[ii[l]];
				return l + 1;
			}
		}
	return n_;
}

int main() {
	int q, i;

	srand_();
	scanf("%d%d", &n, &q);
	for (i = 0; i < n; i++) {
		scanf("%lld%d%d", &aa[i], &ww[i], &vv[i]);
		ii[i] = i;
	}
	sort(ii, 0, n);
	for (i = 0; i < n; i++)
		inv[ii[i]] = i;
	build();
	while (q--) {
		int t;

		scanf("%d", &t);
		if (t == 1 || t == 2) {
			int a;

			scanf("%d%d", &a, &i), i--;
			update_(inv[i], t == 1 ? a : -a);
		} else {
			int lg, i;

			scanf("%lld", &c);
			ans = 0;
			for (lg = LG, i = 0; lg >= 0 && i < n_; lg--)
				i = jump(lg, i);
			printf("%lld\n", ans);
		}
	}
	return 0;
}
