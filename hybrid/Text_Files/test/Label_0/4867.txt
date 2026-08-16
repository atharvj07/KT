#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <utility>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <cstdio>
#include <cstring>

using namespace std;

#define PI acos(-1.0)

int main() {
	int n; cin >> n;
	vector<pair<int, int> > xy(n);
	for (int i = 0; i < n; ++i) cin >> xy[i].first >> xy[i].second;
	sort(xy.begin(), xy.end());
	double alpha = 0, ans = 1e18;
	do {
		alpha = atan2(xy[0].second, xy[0].first);
		if (alpha < 0) alpha += 2 * PI;
		double tmp = min(abs(alpha), 2 * PI - abs(alpha));
		for (int i = 1; i < n; ++i) {
			double t = atan2(xy[i].second - xy[i - 1].second, xy[i].first - xy[i - 1].first);
			if (t < 0) t += 2 * PI;
			tmp += min(abs(alpha - t),2*PI- abs(t - alpha));
			alpha = t;
		}
		double t = atan2(-xy[n - 1].second, -xy[n - 1].first);
		if (t < 0) t += 2 * PI;
		tmp += min(abs(alpha - t), 2 * PI - abs(t - alpha));
		ans = min(ans, tmp);
	} while (next_permutation(xy.begin(), xy.end()));
	printf("%.10f\n", ans * 180.0 / PI);


	return 0;
}
