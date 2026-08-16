#include <bits/stdc++.h>
using namespace std;

const int N = 55;
int n;
long long a[N];
long long ans;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);

	cin >> n;
	for (int i = 1; i <= n; ++i) cin >> a[i];

	bool found = true;
	
	while(found) {
		found = false;
		for (int i = 1; i <= n; ++i) {
			if (a[i] >= n) {
				found = true;
				
				long long add = a[i] / n;
				a[i] %= n;
				ans += add;
				for (int j = 1; j <= n; ++j) {
					if (j != i) a[j] += add;
				}
			}
		}

		if (!found) break;
	}

	cout << ans << endl;
}