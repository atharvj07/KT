#include<iostream>
#include<string>
#include<algorithm>	
#include<cmath>
using namespace std;
int main(void) {
	int n, m, a; cin >> n >> m;
	int test[101] = { 0 };
	for (int h = 0; h < n; h++) {
		cin >> a;
		test[h] = a;
	}
	for (int h = 1; h <= m; h++) {
		for (int i = 0; i < n; i++) {
			if (i != n - 1 &&  test[i] % h > test[i + 1] % h) {
				int uio = test[i];
				test[i] = test[i + 1];
				test[i + 1] = uio;
			}
		}
	}
	for (int h = 0; h < n; h++) {
		cout << test[h] << endl;
	}
}
