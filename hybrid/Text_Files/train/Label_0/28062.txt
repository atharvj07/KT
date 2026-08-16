#include <bits/stdc++.h>
#define REP(i,n,s) for (int i = (s); i < (n); i++)
#define SIZE 201
using namespace std;
typedef long long int LL;

int H, W, A[SIZE][SIZE], dp[2][SIZE][SIZE];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	memset(A, 0, sizeof(A));
	cin >> H >> W;
	REP(i, H, 0) {
		REP(j, W, 0) {
			cin >> A[i][j];
		}
	}

	int pos = 0;
	memset(dp, -1, sizeof(dp));
	dp[pos][0][0] = A[0][0];
	REP(i, H+W-1, 1) {
		pos ^= 1;
		memset(dp[pos], -1, sizeof(dp[pos]));
		REP(j, W, 0) {
			REP(k, W, 0) {
				if (dp[pos^1][j][k] == -1) continue;
				REP(x, j+2, j) {
					REP(y, k+2, k) {
						int s = i - x, t = i - y;
						if (s<0||s>=H||t<0||t>=H||x>=W||y>=W) continue;
						dp[pos][x][y] = max(dp[pos][x][y], dp[pos^1][j][k] + A[s][x] + (s==t?0:A[t][y]));
					}
				}
			}
		}
	}
	cout << dp[pos][W-1][W-1] << endl;
}