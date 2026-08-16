#include <bits/stdc++.h>
using namespace std;
long long memo[5][100005];
int grid[5][100005];
int N;
long long DP(int start, int idx) {
  if (idx == N) {
    if (start == 2)
      return 0;
    else
      return -1000000000000000;
  }
  if (idx > N) return -1000000000000000;
  if (memo[start][idx] != -1) return memo[start][idx];
  long long res = 0;
  if (start == 0) {
    res = DP(0, idx + 1);
    res = max(res, DP(1, idx + 1) + grid[1][idx]);
    res = max(res, DP(2, idx + 1) + grid[1][idx] + grid[2][idx]);
    res = max(res, DP(2, idx + 2) + grid[1][idx] + grid[2][idx] +
                       grid[0][idx + 1] + grid[2][idx + 1] + grid[1][idx + 1]);
  } else if (start == 1) {
    res = DP(1, idx + 1);
    res = max(res, DP(0, idx + 1) + grid[0][idx]);
    res = max(res, DP(2, idx + 1) + grid[2][idx]);
  } else {
    res = DP(2, idx + 1);
    res = max(res, DP(1, idx + 1) + grid[1][idx]);
    res = max(res, DP(0, idx + 1) + grid[1][idx] + grid[0][idx]);
    res = max(res, DP(0, idx + 2) + grid[1][idx] + grid[0][idx] +
                       grid[2][idx + 1] + grid[0][idx + 1] + grid[1][idx + 1]);
  }
  return memo[start][idx] = res + grid[start][idx];
}
int main() {
  memset(memo, -1, sizeof memo);
  ios_base::sync_with_stdio(0);
  cin >> N;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < N; j++) {
      cin >> grid[i][j];
    }
  }
  cout << DP(0, 0);
}
