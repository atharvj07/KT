#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const ll MOD = 1e9 + 7;

int main() {
	ios::sync_with_stdio(0), cin.tie(0);
	int N; cin >> N;
	vector<pair<int, bool>> coords;
	coords.reserve(2*N);
	for (int i = 0; i < N; i++) {
		int a; cin >> a;
		coords.emplace_back(a, false);
	}
	for (int i = 0; i < N; i++) {
		int b; cin >> b;
		coords.emplace_back(b, true);
	}
	sort(coords.begin(), coords.end());
	int cnts[2] = {};
	ll ans = 1;
	for (auto it : coords) {
		bool t = it.second;
		if (cnts[!t]) {
			ans *= cnts[!t];
			ans %= MOD;
			cnts[!t]--;
		} else {
			cnts[t]++;
		}
	}
	cout << ans << '\n';

	return 0;
}
