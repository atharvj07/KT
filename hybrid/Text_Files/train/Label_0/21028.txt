#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
typedef pair<long long int, long long int> P;
#define F first
#define S second
#define MAX_N 100000
#define INF 1e18
P house[2][2 * MAX_N + 1];
long long int ruiseki[2][2 * MAX_N + 1] = {};
int main() {
	long long int w, h, n, sum = 0, time = INF, ma = 0, mid, x = 0, y = 0, ansx = INF, ansy = INF, p, mid2, sum2;

	P save, save2, search;
	cin >> w >> h >> n;
	for (int i = 0; i <2 * n; i += 2) {
		long long int a, b;
		scanf("%lld%lld", &a, &b);
		house[0][i] = make_pair(a, b);
		house[0][i + 1] = house[0][i];
		house[1][i] = make_pair(b, a);
		house[1][i + 1] = house[1][i];
	}
	sort(house[0], house[0] + 2 * n);
	sort(house[1], house[1] + 2 * n);
	for (int i = 0; i < 2 * n; i++) {
		for (int j = 0; j < 2; j++) {
			ruiseki[j][i] += house[j][i].F;
			if (i)
				ruiseki[j][i] += ruiseki[j][i - 1];
		}
	}
	mid = mid2 = n - 1;
	for (int j = 0; j < 2 * n; j += 2) {
		sum2 = 0;
		if (j < mid)
			mid++;
		search = make_pair(house[0][j].S, house[0][j].F);
		p = lower_bound(house[1], house[1] + n * 2, search) - house[1];
		if (p < mid2)
			mid2++;
		x = house[0][mid].F;
		y = house[1][mid2].F;
		sum2 += (mid + 1) * x + (mid2 + 1) * y - ruiseki[0][mid] - ruiseki[1][mid2];
		sum2 += ruiseki[0][2 * n - 1] + ruiseki[1][2 * n - 1] - ruiseki[0][mid] - ruiseki[1][mid2] - (2 * n - mid - 1) * x - (2 * n - mid2 - 1) * y;
		sum2 -= abs(house[0][j].F - x) + abs(house[0][j].S - y);
		if (time == sum2) {
			time = sum2;
			if (ansx > x) {
				ansx = x;
				ansy = y;
			}
			if (ansx == x) {
				if (ansy > y) {
					ansy = y;
				}
			}
		}
		if (time > sum2) {
			time = sum2;
			ansx = x;
			ansy = y;
		}
		if (j < mid)
			mid--;
		if (p < mid2)
			mid2--;
	}
	cout << time << endl;
	cout << ansx << ' ' << ansy << endl;
}