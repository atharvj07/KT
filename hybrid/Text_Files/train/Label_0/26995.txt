#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define MOD 1000000007
#define ADD(X,Y) ((X) = ((X) + (Y)%MOD) % MOD)
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;

int N, A, B, C, D;
i64 dp[2][1010];
i64 Cb[1010][1010];

int main()
{
	scanf("%d%d%d%d%d", &N, &A, &B, &C, &D);
	int t = 0;
	dp[t][N] = 1;

	Cb[0][0] = 1;
	for (int i = 1; i <= N; ++i) {
		Cb[i][0] = 1;
		for (int j = 1; j <= N; ++j) Cb[i][j] = (Cb[i - 1][j - 1] + Cb[i - 1][j]) % MOD;
	}

	for (int i = A; i <= B; ++i) {
		for (int j = 0; j <= N; ++j) dp[1 - t][j] = dp[t][j];

		i64 pat = 1;
		for (int k = 1; k <= D; ++k) {
			if (i * k > N) break;
			pat = pat * Cb[i * k - 1][i - 1] % MOD;
			if (k < C) continue;
			for (int j = i * k; j <= N; ++j) {
				ADD(dp[1 - t][j - i * k], dp[t][j] * pat % MOD * Cb[j][i * k] % MOD);
			}
		}
		t = 1 - t;
	}
	printf("%lld\n", dp[t][0]);

	return 0;
}
