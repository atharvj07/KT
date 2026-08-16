#include <bits/stdc++.h>

using namespace std;
using ll = long long;
#define M ll(1e9+7)

int main() {
	ios::sync_with_stdio(false); cin.tie(0);
	ll n, x; cin >> n;
	unordered_map<ll,int> f;
	for (int i = 0; i < n; i++) {
		cin >> x;
		f[x]++;
	}
	bool flag = true;
	for (ll i = n-1; i > 0; i -= 2) {
		if (f[i] != 2) flag = false;
	}
	if (n&1) {
		flag &= (f[0] == 1);
	}
	if (!flag) {
		cout << "0\n";
	} else {
		ll ans = 1;
		for (int i = 0; i < n/2; i++) {
			ans = (ans * 2) % M;
		}
		cout << ans << "\n";
	}
	return 0;
}