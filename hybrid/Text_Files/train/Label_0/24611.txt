#include <bits/stdc++.h>
using namespace std;
const int maxn = 25;
const int maxs = 1 << 20;
template <typename T>
void chkmax(T &x, T y) {
  x = max(x, y);
}
template <typename T>
void chkmin(T &x, T y) {
  x = min(x, y);
}
template <typename T>
void read(T &x) {
  x = 0;
  int f = 1;
  char c = getchar();
  for (; !isdigit(c); c = getchar())
    if (c == '-') f = -f;
  for (; isdigit(c); c = getchar()) x = x * 10 + c - '0';
  x *= f;
}
int n, u, dp[maxs];
long long a[maxn];
int bit[maxn], cnt[maxs];
long long sum[maxs];
bool check(int s) {
  if (cnt[s] == 1) return sum[s] == 0;
  if ((sum[s] + cnt[s]) % 2 == 0) return false;
  int tmp = s;
  for (int i = 1; i <= n; i++)
    if (bit[i] & s) tmp = s ^ bit[i];
  for (int t = tmp; t != 0; t = (t - 1) & s) {
    long long tmp = sum[t] * 2 - sum[s];
    if (tmp >= -cnt[s] + 1 && tmp <= cnt[s] - 1) return true;
  }
  return false;
}
int main() {
  read(n), u = (1 << n) - 1;
  for (int i = 1; i <= n; i++) read(a[i]), bit[i] = 1 << (i - 1);
  for (int s = 0; s <= u; s++)
    for (int i = 1; i <= n; i++)
      if (bit[i] & s) {
        cnt[s]++;
        sum[s] += a[i];
      }
  for (int s = 1; s <= u; s++) dp[s] = check(s);
  for (int s = 1; s <= u; s++)
    for (int t = (s - 1) & s; t != 0; t = (t - 1) & s)
      chkmax(dp[s], dp[t] + dp[s ^ t]);
  cout << n - dp[u] << endl;
}
