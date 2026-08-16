#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000 * 1000 * 1000 + 7;

int main()
{
	int N, M;
	cin >> N >> M;

	vector<int> S(N), T(M);
	for (auto &x : S) cin >> x;
	for (auto &x : T) cin >> x;

	vector<vector<long long>> dp(N + 1, vector<long long>(M + 1, 0));

	for (int i = 0; i <= N; ++i) {
		dp[i][0] = 1;
	}
	for (int j = 0; j <= M; ++j) {
		dp[0][j] = 1;
	}
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j) {
			dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j]) % MOD;
			if (S[i] != T[j]) {
				dp[i + 1][j + 1] = (dp[i + 1][j + 1] + MOD - dp[i][j]) % MOD;
			}
		}
	}
	cout << dp[N][M] << endl;
}
