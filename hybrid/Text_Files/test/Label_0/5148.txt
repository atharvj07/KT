#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false), cin.tie(0);
	int N, Q;
	cin >> N >> Q;
	int p = 0;
	while (Q--) {
		int t, k;
		cin >> t >> k;
		if (t == 0) {
			printf("%d\n", (p + --k) % N + 1);
		}
		else {
			p = (p + k) % N;
		}
	}
	return 0;
}

