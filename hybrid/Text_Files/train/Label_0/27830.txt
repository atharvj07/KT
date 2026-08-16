#include<iostream>
#include<algorithm>
using namespace std;
int main() {
	int n, a[1010]; cin >> n; for (int i = 0; i < n; i++)cin >> a[i];
	sort(a, a + n);
	for (int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			if ((a[j] - a[i]) % (n - 1) == 0) {
				cout << a[i] << ' ' << a[j] << endl;
				return 0;
			}
		}
	}
	return 0;
}
