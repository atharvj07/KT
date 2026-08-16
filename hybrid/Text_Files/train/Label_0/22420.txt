#include <bits/stdc++.h>

typedef long long int64;

const int MAX_N = int(2e5) + 10;

void fail() {
	puts("-1");
	exit(0);
}

int n;
int a[MAX_N], b[MAX_N];
std::priority_queue<std::pair<int, int> > q;

int main() {
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		scanf("%d", a + i);
	}
	for (int i = 1; i <= n; ++i) {
		scanf("%d", b + i);
		if (a[i] != b[i])
			q.push(std::make_pair(b[i], i));
	}

	int64 ans = 0;
	while (!q.empty()) {
		auto cur = q.top();
		q.pop();
		int i = cur.second, pre = i == 1 ? n : i - 1, nxt = i == n ? 1 : i + 1;
		int t = (b[i] - a[i]) / (b[pre] + b[nxt]);
		if (t == 0) fail();
		ans += t;
		b[i] -= t * (b[pre] + b[nxt]);
		if (a[i] != b[i])
			q.push(std::make_pair(b[i], i));
	}
	printf("%lld\n", ans);
}