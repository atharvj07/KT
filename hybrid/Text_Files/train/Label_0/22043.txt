#include <bits/stdc++.h>
using namespace std;

bool ok(int n) {
	int k = n % 10;
	n /= 10;
	while ( n ) {
		if ( n % 10 != k-1 ) return false;
		k = n % 10;
		n /= 10;
	}

	return true;
}

int main() {
	int n;
	cin >> n;

	vector<int> v(n);
	for ( int i = 0; i < n; i++ ) cin >> v[i];

	int ans = -1;
	for ( int i = 0; i < n; i++ ) {
		for ( int j = i+1; j < n; j++ ) {
			int p = v[i]*v[j];\
			//cout << p << endl;
			if ( ok(p) ) ans = max(ans, p);
		}
	}

	cout << ans << endl;
	return 0;
}

