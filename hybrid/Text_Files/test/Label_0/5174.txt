#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define int long long
using namespace std;
int n, k, a[123456], b[123456];
signed main() {
	cin >> n >> k;
	for (int i = 0; i < n; i++)cin >> a[i];
	int f = 0, l = 0, ans = n + 1, sum = 0;
	while (f < n) {
		while (sum < k && l < n) {
			if (a[l] <= k && b[a[l]] == 0)sum++;
			b[a[l++]]++;
		}
		if (sum < k)break;
		ans = min(ans, l - f);
		if (a[f] <= k && b[a[f]] == 1)sum--;
		b[a[f++]]--;
	}
	if (ans > n)cout << "0\n";
	else cout << ans << endl;
}
