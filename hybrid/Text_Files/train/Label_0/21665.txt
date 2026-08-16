#include <cmath>
#include <iostream>
using namespace std;
const long double eps = 1.0e-5L;
int Q; long double a, b, c, d;
int main() {
	cin >> Q;
	while (Q--) {
		cin >> a >> b >> c >> d;
		b *= 1 / a, c *= 1 / a, d *= 1 / a;
		long double l = -1.0e+6L, r = 1.0e+6L;
		for (int i = 0; i < 70; i++) {
			long double m = (l + r) / 2;
			if (m * m * m + b * m * m + c * m + d > 0) r = m;
			else l = m;
		}
		long double g1 = b + l, g0 = c + b * l + l * l;
		long double e = g1 * g1 - 4 * g0;
		int ret1 = 0, ret2 = 0;
		if (l > eps) ret1++;
		if (l < -eps) ret2++;
		if (e > -eps) {
			long double s = (e > eps ? sqrt(e) : 0);
			long double t1 = (-g1 - s) / 2;
			long double t2 = (-g1 + s) / 2;
			if (t1 > eps) ret1++;
			if (t1 < -eps) ret2++;
			if (t2 > eps) ret1++;
			if (t2 < -eps) ret2++;
		}
		cout << ret1 << ' ' << ret2 << endl;
	}
	return 0;
}