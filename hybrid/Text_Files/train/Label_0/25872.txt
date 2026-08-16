#include <iostream>

using namespace std;

int main() {
	int n; cin >> n;
	int h, max = 0, ans = 0;
	for (int i = 0; i < n; ++i) {
		cin >> h;
		if (max <= h) {
			ans++;
			max = h;
		}
	}
	cout << ans << endl;

	return 0;
}