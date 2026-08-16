#include <bits/stdc++.h>
using namespace std;
const int N = 2e4 + 10, mod = 1e9 + 7, M = 510;
const double PI = 3.1415926535;
long long res[40], p[40], ei[40], sum[N], cnt;
double pre[N];
int path[100];
void dfs(int u, int s, long long va) {
  if (u == -1) {
    sum[s] = ((long long)sum[s] + va) % mod;
    return;
  }
  for (int i = 0; i <= cnt; i++) {
    path[i]++;
    if (res[i] - path[i] + 1)
      dfs(u - 1, s + i, (long long)va * (res[i] - path[i] + 1) % mod);
    path[i]--;
  }
}
int main() {
  int n;
  scanf("%d", &n);
  vector<int> temp;
  int t = n;
  while (t) t /= 10, cnt++;
  p[1] = 1;
  for (int i = 2; i <= 11; i++) p[i] = p[i - 1] * 10;
  ei[0] = 1;
  for (int i = 1; i < 11; i++) ei[i] = ei[i - 1] * 8;
  for (int i = 0; i < (1 << cnt); i++) {
    vector<int> temp;
    for (int j = 0; j < cnt; j++)
      if (i >> j & 1) temp.push_back(j);
    int len = temp.size();
    for (int j = 0; j < 1 << len; j++) {
      int a[15] = {0};
      for (int k = 0; k < len; k++)
        if (j >> k & 1)
          a[temp[k]] = 7;
        else
          a[temp[k]] = 4;
      long long f = p[cnt], va = 0;
      for (long long k = cnt - 1, r = 1; k >= 0; k--, r *= 10)
        va += (long long)a[k] * r;
      if (va > n) continue;
      for (int k = 0; k < cnt; k++) {
        if (a[k]) {
          f /= 10;
          continue;
        }
        for (int r = 9; r >= 0; r--)
          if ((long long)r * f + va <= n) {
            a[k] = r, va = r * f + va;
            break;
          }
        f /= 10;
      }
      long long num = 0, ans = 0;
      for (int k = 0; k < cnt; k++) {
        if (num < temp.size() && temp[num] == k) {
          num++;
          if (k == cnt - 1) ans++;
          continue;
        }
        if (a[k] == 7 || a[k] == 4) {
          int sum = cnt - 1 - k;
          int ts = temp.size() - num;
          int tnum = a[k] + 1;
          if (a[k] == 4)
            tnum--;
          else
            tnum -= 2;
          ans = ans + ei[sum - ts] * (long long)tnum;
          break;
        } else {
          int sum = cnt - 1 - k;
          int ts = temp.size() - num;
          int tnum = a[k] + 1;
          if (a[k] > 7)
            tnum -= 3;
          else if (a[k] > 4)
            tnum -= 2;
          else
            tnum--;
          if (k == cnt - 1) tnum++;
          ans = ans + ei[sum - ts] * (long long)tnum;
        }
      }
      res[len] = (res[len] + (long long)ans);
    }
  }
  res[0]--;
  dfs(5, 0, 1);
  long long ans = 0, pre = 0;
  for (int i = 1; i <= cnt; i++) {
    pre = pre + sum[i - 1];
    ans = (ans + pre * res[i]) % mod;
  }
  cout << ans << endl;
  return 0;
}
