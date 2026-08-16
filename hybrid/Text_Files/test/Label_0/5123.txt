#include <bits/stdc++.h>
using namespace std;
const int Maxn = 1e5 + 10;
const int Inf = 0x7f7f7f7f;
const long long Inf_ll = 1ll * Inf * Inf;
const int Mod = 1e9 + 7;
const double eps = 1e-7;
int a[200][10];
int cnt[10];
int book[10];
int score(int p, int idx) {
  double rate = (double)cnt[idx] / p;
  if (rate - 0.5 > eps)
    return 500;
  else if (rate - 0.25 > eps)
    return 1000;
  else if (rate - 0.125 > eps)
    return 1500;
  else if (rate - 1.0 / 16 > eps)
    return 2000;
  else if (rate - 1.0 / 32 > eps)
    return 2500;
  return 3000;
}
int getscore(int f, int num) {
  int ret = 0;
  for (int i = 1; i <= 5; ++i) {
    if (a[f][i] == -1) continue;
    ret += score(num, i) - score(num, i) / 250 * a[f][i];
  }
  return ret;
}
int n;
bool check(int k) {
  for (int i = 1; i <= 5; ++i) {
    if (book[i] == 1) cnt[i] += k;
  }
  int a = getscore(1, k + n);
  int b = getscore(2, k + n);
  for (int i = 1; i <= 5; ++i) {
    if (book[i] == 1) cnt[i] -= k;
  }
  return a > b;
}
int flag[5];
int main() {
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= 5; ++j) {
      scanf("%d", &a[i][j]);
      if (a[i][j] >= 0) cnt[j]++;
    }
  }
  for (int i = 1; i <= 5; ++i) {
    if (a[1][i] >= 0 && a[2][i] >= 0) {
      if (a[1][i] >= a[2][i])
        book[i] = 1;
      else
        book[i] = 2;
    }
  }
  for (int i = 0; i <= 6500; ++i) {
    if (check(i)) {
      printf("%d\n", i);
      return 0;
    }
  }
  puts("-1");
  return 0;
}
