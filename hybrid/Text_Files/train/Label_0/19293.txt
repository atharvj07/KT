#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll a[10], ans;
int main()
{
	for(int i = 1; i <= 7; ++i) cin >> a[i]; 
	ll ans1 = a[2] + 2 * ((a[1] / 2) + (a[4] / 2) + (a[5] / 2));
	if(a[1] && a[4] && a[5])
	{
		--a[1], --a[4], --a[5];
		ll ans2 = a[2] + 2 * ((a[1] / 2) + (a[4] / 2) + (a[5] / 2)) + 3;
		cout << max(ans1, ans2) << endl;
	}
	else cout << ans1 << endl;
	return 0;
}