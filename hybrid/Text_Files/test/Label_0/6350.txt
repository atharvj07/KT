#include<bits/stdc++.h>
using namespace std;
#define int long long
const int maxn = 2e5 + 7;
int a[maxn];
signed main () {
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		for (int i = 1; i <= n; i++) cin >> a[i];
		map<int,int>mp;
		mp.clear();
		int ans = 0;
		for (int i = 1; i <= n; i++) {
			ans += mp[a[i]] * (n-i+1);
			mp[a[i]] += i;
		}
		cout << ans << "\n";
	}
}