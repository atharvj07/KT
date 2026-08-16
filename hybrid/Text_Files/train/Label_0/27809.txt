#include <iostream>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;

int dfs(int n, int sum, int k, int sn) {
	int ret = 0;
	if ( k < 0 ) {
		return 0;
	}
	else {
		if (sn == sum) {
			return 1;
		}
	}
	if (sn > sum || n == 0) {
		return 0;
	}
	if ( sn + (k * pow(n,2)) < sum ) {
		return 0;
	}

	ret += dfs(n, sum, k-1, sn+pow(n,2));
	ret += dfs(n-1, sum, k, sn);
	
	return ret;
}

int main(void) {
	int n;
	cin >> n;

	int lim,ret;
	bool find = false;
	while ( n != 0 ) {
		find = false;
		for (int i = 1; !(find); i++) {
			if ( !(pow(i,2) < n) ) {
				lim = i;
				find = true;
			}
		}
		ret = dfs(lim, n, 4, 0);
		cout << ret << endl;
		cin >> n;
	}
	return 0;
}