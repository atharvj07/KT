#define  _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstring>
#include <queue>
#include <stack>
#include <math.h>
#include <iterator>
#include <vector>
#include <string>
#include <set>
#include <math.h>
#include <iostream>
#include <random>
#include<map>
#include <iomanip>
#include <time.h>
#include <stdlib.h>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
#include <cassert>
#include<fstream>
#include <unordered_map>
#include <cstdlib>
#include <complex>
#include <cctype>
using namespace std;
typedef string::const_iterator State;
#define Ma_PI 3.141592653589793
#define eps 0.00000001
#define LONG_INF 1e18
#define GOLD 1.61803398874989484820458
#define MAX_MOD 1000000007
#define MOD 998244353
#define seg_size 262144
#define REP(i,n) for(long long i = 0;i < n;++i)
vector<int> vertexs[200000];
long long dp[200000][301][2] = {};
long long pre_dp[701][2] = {};
int cnter[200000];
int dfs(int now, int back) {
	cnter[now] = 1;
	for (int i = 0; i < vertexs[now].size(); ++i) {
		if (vertexs[now][i] == back) continue;
		cnter[now] += dfs(vertexs[now][i], now);
	}
	cnter[now] = min(cnter[now], 300);
	REP(i, 601) {
		REP(q, 2) {
			pre_dp[i][q] = 0;
		}
	}
	pre_dp[0][0] = 1;
	pre_dp[0][1] = 1;
	int now_max = 0;
	for (int i = 0; i < vertexs[now].size(); ++i) {
		if (vertexs[now][i] == back) continue;
		for (int q = now_max; q >= 0;--q) {
			long long geko_a = pre_dp[q][0];
			long long geko_b = pre_dp[q][1];
			pre_dp[q][0] = 0;
			pre_dp[q][1] = 0;
			for (int j = 0; j <= cnter[vertexs[now][i]]; ++j) {
				pre_dp[q + j][0] += (geko_a * dp[vertexs[now][i]][j][0])%MOD;
				pre_dp[q + j][0] %= MOD;
				pre_dp[q + j + 1][0] += (geko_a * dp[vertexs[now][i]][j][1])%MOD;
				pre_dp[q + j + 1][0] %= MOD;
				pre_dp[q + j][1] += (geko_b * dp[vertexs[now][i]][j][1])%MOD;
				pre_dp[q + j][1] %= MOD;
				pre_dp[q + j+1][1] += (geko_b * dp[vertexs[now][i]][j][1]) % MOD;
				pre_dp[q + j+1][1] %= MOD;
				pre_dp[q + j][1] += (geko_b * dp[vertexs[now][i]][j][0])%MOD;
				pre_dp[q + j][1] %= MOD;
			}
		}
		now_max += cnter[vertexs[now][i]];
		now_max = min(now_max, 300);
	}
	REP(i, 301) {
		REP(q, 2) {
			dp[now][i][q] = pre_dp[i][q];
		}
	}
	return cnter[now];
}
int main(){
	long long n, k;
	cin >> n >> k;
	REP(i, n-1) {
		int a, b;
		cin >> a >> b;
		a--;
		b--;
		vertexs[a].push_back(b);
		vertexs[b].push_back(a);
	}
	dfs(0, -1);
	cout << (dp[0][k][0] + dp[0][k - 1][1]) % MOD << endl;
	return 0;
}
