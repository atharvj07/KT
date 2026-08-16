#include<bits/stdc++.h>
using namespace std;
using UL = unsigned int;
using ULL = unsigned long long;
using LL = long long;
#define rep(i, n) for(UL i = 0; i < (n); i++)

struct Problem {
public:

	void Solve() {
		while (true) {
			UL N; scanf("%d", &N);
			if (N == 0) break;
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			int X, Y; scanf("%d%d", &X, &Y);
			int ans = 0;
			rep(i, N) {
				int x, y; scanf("%d%d", &x, &y);
				int a, b, c;
				a = max(x1 - x, max(x - x2, 0)) + max(y1 - y, max(y - y2, 0));
				b = max(x1 - X, max(X - x2, 0)) + max(y1 - Y, max(Y - y2, 0));
				b = max(b - 1, 0);
				c = abs(X - x) + abs(Y - y);
				ans += min(a + b, c);
				X = x; Y = y;
			}
			printf("%d\n", ans);
		}
	}
};

int main() {
	unique_ptr<Problem> p(new Problem());
	p->Solve();
	return 0;
}

