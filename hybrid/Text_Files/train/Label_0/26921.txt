#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <numeric>
#include <cctype>
#include <tuple>
#include <array>
#include <climits>
#include <bitset>

// BEGIN CUT HERE
#ifdef _MSC_VER
#include <agents.h>
#endif
// END CUT HERE 

#define FOR(i, a, b) for(int i = (a); i < (int)(b); ++i)
#define rep(i, n) FOR(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define REV(v) v.rbegin(), v.rend()
#define MEMSET(v, s) memset(v, s, sizeof(v))
#define MP make_pair
#define MT make_tuple

using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;

const int N = 1010;
int dp[N];
vector<int> G[N];

int calc_grundy(int v);

void dfs(int v, int x, set<int> &st){
	for (auto nxt : G[v]){
		x ^= calc_grundy(nxt);
	}
	st.insert(x);
	for (auto nxt : G[v]){
		dfs(nxt, x^calc_grundy(nxt), st);
	}
}

int calc_grundy(int v){
	int &res = dp[v];
	if (res >= 0) return res;

	set<int> st;
	dfs(v, 0, st);
	for (int i = 0; i <= 1000; ++i){
		if (st.count(i) == 0) return res = i;
	}
	return -1;
}

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);

	MEMSET(dp, -1);

	int n, m;
	cin >> n >> m;

	vector<int> p(n, -1);
	rep(i, m){
		cin >> p[i];
		--p[i];
		G[p[i]].push_back(i);
	}

	int g = 0;
	rep(i, n) if (p[i] < 0) g ^= calc_grundy(i);

	cout << (g ? "Alice" : "Bob") << endl;

	return 0;
}
