#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	int count = 0;
	for (int i = n - 1; i >= 0; i--) {
		for (int j = i * 2 + 1; j < n; j += i + 1) {
			a[i] ^= a[j];
		}
		count += a[i];
	}
	cout << count << endl;
	for (int i = 0; i < n; i++) {
		if (a[i])
			cout << i + 1 << " ";
	}

}
