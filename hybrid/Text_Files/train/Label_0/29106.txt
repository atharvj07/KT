#include <bits/stdc++.h>
using namespace std;
const long long INF = 1LL << 62;
const int MAX = 1e3 + 3;
int grid[MAX][MAX];
void solve() {
  memset(grid, 0, sizeof(grid));
  int n, a, b;
  cin >> n >> a >> b;
  if (a > 1 && b > 1) {
    cout << "NO" << endl;
    return;
  }
  if (a == 1 && b == 1 && (n == 3 || n == 2)) {
    cout << "NO" << endl;
    return;
  }
  if (a == 1 && b == 1) {
    for (long long i = (long long)(0); i < (long long)(n - 1); i++)
      grid[i][i + 1] = 1, grid[i + 1][i] = 1;
  } else if (b == 1) {
    for (long long i = (long long)(0); i < (long long)(n - a); i++)
      grid[i][i + 1] = 1, grid[i + 1][i] = 1;
  } else if (a == 1) {
    for (long long i = (long long)(0); i < (long long)(n); i++)
      for (long long j = (long long)(0); j < (long long)(n); j++)
        grid[i][j] = 1;
    for (long long i = (long long)(0); i < (long long)(n); i++) grid[i][i] = 0;
    for (long long i = (long long)(0); i < (long long)(n - b); i++)
      grid[i][i + 1] = 0, grid[i + 1][i] = 0;
  }
  cout << "YES" << endl;
  for (long long i = (long long)(0); i < (long long)(n); i++) {
    for (long long j = (long long)(0); j < (long long)(n); j++) {
      cout << grid[i][j];
    }
    cout << endl;
  }
  return;
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  int t = 1;
  while (t--) solve();
  return 0;
}
