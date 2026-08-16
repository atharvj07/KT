#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())
typedef long long ll;

int n, d;
ll t[100005], f[100005];

int main(int argc, char const *argv[]) {
	ios_base::sync_with_stdio(false);
	cin >> n >> d;
	FOR(i, n) {
		cin >> t[i] >> f[i];
		f[i]--;
	}
	ll ti = 0, pos = 0, ret = 0;
	int cnt = 0;
	FOR(i, n) {
		if (t[i] >= ti + pos + f[i]) {
			ti += pos;
			for (int j = i-1; j >= i-cnt; j--) ret += ti-t[j];
			cnt = 1;
		}
		else {
			if (cnt+1 > d || t[i] < ti + abs(f[i] - pos)) {
				cout << -1 << endl;
				return 0;
			}
			cnt++;
		}
		pos = f[i];
		ti = t[i];
	}
	ti += pos;
	for (int i = n-1; i >= n-cnt; i--) ret += ti-t[i];
	cout << ret << endl;
	return 0;
}