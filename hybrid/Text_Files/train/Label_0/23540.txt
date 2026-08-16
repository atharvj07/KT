#include <bits/stdc++.h>
using namespace std;
const int MOD9 = 1e9 + 7;
const int MOD91 = 1e9 + 9;
const long long MOD12 = 1e12 + 39LL;
const long long MOD15 = 1e15 + 37LL;
const int INF = 1e9;
const int base = 1e9;
const int MAX = 2e5;
const long double EPS = 1e-10;
int n, m;
int a[20][200];
int b[20];
int c[20];
int d[20];
int e[20];
int maxs = 0;
char ch;
int dpt[20][3];
int dp(int stage, int lr) {
  if (stage == maxs) {
    if (lr == 0) {
      return (c[stage]);
    } else {
      return (e[stage]);
    }
  }
  if (dpt[stage][lr] != -1) {
    return dpt[stage][lr];
  }
  if (lr == 0) {
    return dpt[stage][lr] = min(2 * (c[stage]) + 1 + dp(stage - 1, 0),
                                dp(stage - 1, 1) + m + 2);
  } else {
    return dpt[stage][lr] = min(2 * (e[stage]) + 1 + dp(stage - 1, 1),
                                dp(stage - 1, 0) + m + 2);
  }
}
int main() {
  cin >> n >> m;
  maxs = n - 1;
  for (int i = n - 1; i >= 0; --i) {
    for (int j = 0; j < m + 2; ++j) {
      cin >> ch;
      a[n - 1 - i][j] = ch - '0';
      if (a[n - 1 - i][j] == 1 && maxs == n - 1) maxs = n - 1 - i;
    }
  }
  for (int i = n - 1; i >= 0; --i) {
    for (int j = 0; j < m + 2; ++j) {
      if (a[n - 1 - i][j]) {
        e[n - 1 - i] = m + 1 - j;
        break;
      }
    }
    for (int j = m + 1; j >= 0; --j) {
      if (a[n - 1 - i][j]) {
        c[n - 1 - i] = j;
        break;
      }
    }
  }
  memset(dpt, -1, sizeof(dpt));
  cout << dp(n - 1, 0);
  return 0;
}
