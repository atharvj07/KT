#include <bits/stdc++.h>
using namespace std;

typedef long double ld;
typedef long long lint;

#define PI 3.141592653589793238l

const int MAXN = 3010;

int T[MAXN];
ld X[MAXN], Y[MAXN];

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	int N, L;

	cin >> N >> L;
	for(int i = 0; i < N; i++) cin >> T[i];

	ld ansx = 0, ansy = 0;
	lint cnt = 0;
	for(int i = 0; i < N; i++) for(int j = i + 1; j < N; j++) {
		int k = (j - i - 1) - (N - j + i - 1);
		ansx += k * cos(PI * (T[i] + T[j]) / L);
		ansy += k * sin(PI * (T[i] + T[j]) / L);
		cnt += k;
	}
	cout << fixed;
	cout.precision(50);
	cout << ansx / cnt << " " << ansy / cnt << "\n";
	return 0;
}
