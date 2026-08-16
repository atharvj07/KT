#include<iostream>
#include<iomanip>
#include<algorithm>
#include<array>
#include<bitset>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<functional>
#include<limits>
#include<list>
#include<map>
#include<numeric>
#include<set>
#include<stack>
#include<string>
#include<sstream>
#include<unordered_map>
#include<queue>
#include<vector>
using namespace std;

//#define int long long
using ll = long long;
using ull = unsigned long long;
using pii = pair<int, int>;

#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define rrep(i,a,b) for(int i=(b)-1;i>=(a);i--)
#define all(a) (a).begin(),(a).end()
#define dump(o) {cerr<<#o<<" "<<o<<endl;}
#define dumpc(o) {cerr<<#o; for(auto &e:(o))cerr<<" "<<e;cerr<<endl;}
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
const int MOD = 100000;

signed main() {
	int dp[55][3010] = {};
	for (int N, M, S; cin >> N >> M >> S&&N;) {
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1;
		rep(m, 1, M + 1) {
			rrep(i, 1, N*N + 1) {
				rep(j, 0, S + 1) {
					if (j + m > S)break;
					(dp[i][j + m] += dp[i - 1][j]) %= MOD;
				}
			}
		}
		cout << dp[N*N][S] << endl;
	}
	return 0;
}