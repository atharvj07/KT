//#pragma GCC optimize ("O3", "unroll-loops")
//#pragma GCC target ("avx2")
//#pragma comment(linker, "/stack:200000000")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#include <bits/stdc++.h>
#define LL long long
#define PII pair<int, int>
#define PLL pair<LL, LL>
#define all_of(v) (v).begin(), (v).end()
#define sort_unique(c) (sort(c.begin(),c.end()), c.resize(distance(c.begin(),unique(c.begin(),c.end()))))
#define fi first
#define se second
const int MAXN = (int)1e7 + 9487;
//const LL INF = (LL) 1e9 + 8763;
//const LL MOD = (LL) 998244353;
using namespace std;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
#define div dddivvvvvvvvvv
 
int mpf[MAXN], pw[MAXN], ans[MAXN];
LL div[MAXN];
vector<int> P;

void solve() {
	int c;
	cin >> c;
	cout << ans[c] << '\n';
}

void prep() {
	for (int i = 1; i < MAXN; i++) {
		ans[i] = -1;
		mpf[i] = i;
	}
	
	div[1] = 1, pw[1] = 1;
	for (int i = 2; i < MAXN; i++) {
		ans[i] = -1;
		if (mpf[i] == i) {
			P.push_back(i);
			pw[i] = i;
			div[i] = (i + 1);
		}
		
//		assert(i % pw[i] == 0 && i / pw[i] % mpf[i] != 0);
//		if (i <= 10000000) {
//			LL sum = 0;
//			for (LL x = 1; x * x <= i; x++) {
//				if (i % x == 0) {
//					sum += x;
//					if (x != i / x) {
//						sum += i / x;
//					}
//				}
//			}
//			
//			if (sum != div[i]) {
//				cout << "WTF " << i << " -> " << sum << ' ' << div[i] << endl;
//			}
////			cout << "CHK " << i << endl;
//		}
		
		for (int p : P) {
			if ((LL)i * p >= MAXN) {
				break;
			}
			mpf[i * p] = p;
			if (i % p == 0) {
				pw[i * p] = pw[i] * p;
				div[i * p] = div[i / pw[i]] * (((LL)pw[i * p] * p - 1) / (p - 1));
				break;
			}
			else {
				pw[i * p] = p;
				div[i * p] = div[i] * (1 + p);
			}
		}
	}
	for (int i = MAXN - 1; i >= 1; i--) {
		if (div[i] < MAXN) {
			ans[div[i]] = i;
		}
	}
}
 
int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);

	prep();
	int tc = 1;
	cin >> tc;
	for (int i = 1; i <= tc; i++) {
		solve();
	}
 
	return 0;
} 