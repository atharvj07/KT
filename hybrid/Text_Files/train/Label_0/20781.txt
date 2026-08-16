#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>
#include <fstream>
#include <iterator>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())
#define ten(x) ((int)1e##x)
#define tenll(x) ((ll)1e##x)

int x[5000], a[5000];
int dp[2][5010];
const int MOD = ten(9) + 7;

int main(){
	int n, l;
	scanf("%d%d", &n, &l);
	FOR(i, n) scanf("%d", x + i);
	FOR(i, n) scanf("%d", a + i);
	FOR(i, n) x[i]++;

	FOR(i,l+1) dp[0][i] = 1;
	auto pv = dp[0], nt = dp[1];
	FOR(i, n){
		memset(nt, 0, sizeof(dp[0]));
		if (a[i]) {
			for (int dist = 0; x[i] + dist <= l; dist += a[i]) {
				int cur = x[i] + dist;
				nt[cur] = pv[cur - 1];
			}
		} else {
			nt[x[i]] = pv[x[i] - 1];
		}
		FOR(j, l){
			nt[j + 1] += nt[j];
			if (nt[j + 1] >= MOD)  nt[j + 1] -= MOD;
		}
		swap(pv, nt);
	}
	cout << pv[l] << endl;
}