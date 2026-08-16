#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long int ulli;

int main() {
	ulli n, ans = 0;
	cin >> n;
	map<int, int> m;
	for (ulli i = 1; i <= n; i++) {
		int temp;
		cin >> temp;
		ans += m[i-temp];
		m[i+temp]++;
	}
	cout << ans;
}