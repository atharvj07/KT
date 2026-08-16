#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <functional>
#include <numeric>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <complex>
#include <fstream>

using namespace std;

#define FOR(i,a,b) for(long long i=(a);i<(b);i++)
#define REP(i,N) for(long long i=0;i<(N);i++)
#define ALL(s) (s).begin(),(s).end()
#define fi first
#define se second

#define PI acos(-1.0)
#define INF 1000000007
#define MOD 1000000007
#define EPS 1e-10
#define MAX_N 100100
#define MAX_M 100100

typedef long long ll;
typedef pair<ll, ll> P;
typedef pair<double, double> PD;
typedef pair<string, ll> PS;
typedef vector<ll> V;
typedef pair<P, char> PC;
typedef pair<ll, string> PLS;

int n, c;

int dp[100][(1 << 16) + 10];

int bitnum(int mask){
	int res = 0;
	while (mask > 0){
		res += mask & 1;
		mask >>= 1;
	}
	return res;
}

int main(){
	while (cin >> n >> c&&n + c){
		vector<int> a(n), b(c);
		REP(i, n){
			REP(j, 16){
				int t;
				cin >> t;
				if (t == 1){
					a[i] |= (1 << j);
				}
			}
		}
		REP(i, c){
			REP(j, 16){
				int t;
				cin >> t;
				if (t == 1){
					b[i] |= (1 << j);
				}
			}
		}
		REP(i, 100){
			REP(mask, (1 << 16) + 10){
				dp[i][mask] = -INF;
			}
		}
		dp[0][a[0]] = 0;

		REP(i, n){
			REP(j, c){
				REP(mask, (1 << 16)){
					if (dp[i][mask] == -INF)continue;
					int nxt = mask - (mask&b[j]);
					if (i < n - 1){
						nxt |= a[i + 1];
					}
					dp[i + 1][nxt] = max(dp[i + 1][nxt], dp[i][mask] + bitnum((mask&b[j])));
				}
			}
		}

		int ans = 0;
		REP(i, (1 << 16)){
			if (dp[n][i] != -INF)ans = max(ans, dp[n][i]);
		}
		cout << ans << endl;
	}
}

//struct pic
//
//int N;
//
//int main(){
//	while (cin >> N&&N){
//		REP(i, N - 1){
//			int n, d;
//			cin >> n >> d;
//
//		}
//	}
//}