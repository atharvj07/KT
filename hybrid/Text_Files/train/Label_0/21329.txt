#include <bits/stdc++.h>

typedef std::pair <int, int> pr;
const int N = 200054;

int n, R;
int cnt = 0, r[N];
pr a[N];
std::priority_queue <int, std::vector <int>, std::greater <int> > pq;

int main() {
	int i, x, y, z = 0;
	scanf("%d%d", &n, &R);
	for (i = 0; i < n; ++i) scanf("%d%d", &x, &y), a[i] = pr(x, y);
	std::sort(a, a + n);
	for (x = 1, i = 0; i < n; ++i) {
		pq.emplace(a[i].second);
		if (x <= a[i].first) ++x;
		else r[cnt++] = pq.top(), pq.pop();
	}
	std::sort(r, r + cnt, std::greater <int> ());
	for (y = R, i = 0; i < cnt && x <= y; ++i) r[i] <= y ? --y : ++z;
	printf("%d\n", z + cnt - i);
	return 0;
}