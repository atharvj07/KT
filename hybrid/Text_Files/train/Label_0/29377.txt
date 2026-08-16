#include <iostream>
using namespace std;

int main () {
	int n, s;
	while (cin >> n >> s, n || s) {
		int r[n];
		for (int i = 0; i < n; i++) {
			cin >> r[i];
		}
		int count = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (r[i] + r[j] > s) {
					count++;
				}
			}
		}
		cout << count << endl;
	}
	return 0;
}