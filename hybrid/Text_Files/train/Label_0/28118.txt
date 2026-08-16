#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false), cin.tie(nullptr);

	int t; cin >> t;
	while(t--) {
		int even = 0, odd = 0;
		int n; cin >> n;
		for(int i = 0; i < 2 * n; i++) {
			int x; cin >> x;
			even += x % 2 == 0;
			odd += x % 2 == 1;
		}
		if(even == odd) {
			cout << "Yes" << "\n";
		} else {
			cout << "No" << "\n";
		}
	}
	return 0; 
}
