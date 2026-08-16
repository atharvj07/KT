#include <bits/stdc++.h>

using namespace std;

int n, k;
long long ans1 = 0, ans2 = 0;

int main() {
	cin >> n >> k;
	for (int a = 1; a <= n; ++a) if (2*a % k == 0) {
		long long num = (n-a)/k;
		ans1 += (num+1)*num*3;
		ans2++;
	}
	cout << ans1+ans2 << endl;
	return 0;
}