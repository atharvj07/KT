#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <functional>
#include <map>
using namespace std;

long long H, W, A[509][509], sum;

int main() {
	cin >> H >> W;
	for (int i = 1; i <= H; i++) {
		for (int j = 1; j <= W; j++) {
			cin >> A[i][j];
			long long S1 = 1LL * i * (H + 1 - i);
			long long S2 = 1LL * j * (W + 1 - j);
			sum += A[i][j] * S1 * S2;
		}
	}
	cout << sum << endl;
	return 0;
}
