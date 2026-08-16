#include <iostream>
using namespace std;

int main() {
	string s;
	cin >> s;
	int n = s.size();
	int ans = n;
	for (int i = 1; i < n; i++) {
		if (s[i-1] == s[i]) continue;
		int now = max(i, n-i);
		ans = min(ans, now);
	}
	cout << ans << endl;
	return 0;
}