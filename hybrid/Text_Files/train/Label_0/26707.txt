#include <bits/stdc++.h>
using namespace std;
const int OO = 1 << 28;
int di[] = {1, 0, -1, 0};
int dj[] = {0, 1, 0, -1};
int n, r;
int arr[51];
double dp[51][51][2];
int len;
long long choose(unsigned n, unsigned k) {
  static vector<vector<long long> > mem;
  if (n < k) return 0;
  if (mem.size() <= n) mem.resize(n + 1);
  if (mem[n].size() <= k) mem[n].resize(k + 1, 0);
  if (k == 0) return 1;
  if (mem[n][k]) return mem[n][k];
  if (k == 1)
    return n;
  else if (n == k)
    return 1;
  else
    return mem[n][k] = choose(n - 1, k - 1) + choose(n - 1, k);
}
double calc(int idx, int rem, bool solved) {
  if (idx == r) return rem ? 0 : solved;
  double &x = dp[idx][rem][solved];
  if (x == x) return x;
  x = 0;
  for (int i = 0; i < rem + 1; ++i) {
    int qs = (i + arr[idx] - 1) / arr[idx];
    if (qs > len) break;
    int remOwad = r - idx;
    double p = 1.0 / remOwad;
    x += choose(rem, i) * pow(p, i) * pow(1 - p, rem - i) *
         calc(idx + 1, rem - i, solved | (qs == len));
  }
  return x;
}
int main() {
  cin >> n >> r;
  for (int i = 0; i < r; ++i) cin >> arr[i];
  double res = 0;
  for (int i = 1; i <= n; ++i) {
    memset(dp, -1, sizeof(dp));
    len = i;
    res += calc(0, n, 0) * i;
  }
  printf("%.11lf\n", res);
  return 0;
}
