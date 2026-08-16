#define _USE_MATH_DEFINES
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <cfloat>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <vector>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> i_i;
typedef pair<ll, int> ll_i;
typedef pair<double, int> d_i;
typedef pair<ll, ll> ll_ll;
typedef pair<double, double> d_d;
struct edge { int u, v; ll w; };

ll MOD = 1000000007;
ll _MOD = 1000000009;
int INF = INT_MAX / 2;
double EPS = 1e-10;

bool f(int l, int r, int j, vector<int>& x, vector<int>& a, vector<int>& b, vector<int>& c, vector<vector<vector<int> > >& memo) {
	if (memo[l][r][j] != -1) return memo[l][r][j];
	if (r - l == 1 && x[l] == a[j]) return memo[l][r][j] = 1;
	for (int m = l + 1; m <= r - 1; m++)
		if (f(l, m, b[j], x, a, b, c, memo) && f(m, r, c[j], x, a, b, c, memo))
			return memo[l][r][j] = 1;
	return memo[l][r][j] = 0;
}

int main() {
	int N; cin >> N;
	vector<int> x(N);
	for (int i = 0; i < N; i++)
		cin >> x[i];
	int M; cin >> M;
	vector<int> a(M), b(M), c(M);
	for (int j = 0; j < M; j++) {
		cin >> a[j] >> b[j] >> c[j];
		b[j]--; c[j]--;
	}
	vector<vector<vector<int> > > memo(N + 1, vector<vector<int> >(N + 1, vector<int>(M, -1)));
	cout << (f(0, N, 0, x, a, b, c, memo) ? "Yes" : "No") << endl;
}