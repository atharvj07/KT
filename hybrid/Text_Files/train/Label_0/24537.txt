#include <bits/stdc++.h>
using namespace std;
const int maxn = 1e6 + 10;
const long long mod = 1e9 + 7;
const int inf = 0x3f3f3f3f;
const long long INF = 0x3f3f3f3f3f3f3f3f;
const double eps = 1e-7;
long long n, k, m, T;
int cnt = 0;
vector<int> edge[maxn];
long long mp[2000][2000];
long long judge[2000][2000];
int arr[maxn];
char str[maxn];
long long GCD(long long a, long long b) {
  while (b ^= a ^= b ^= a %= b)
    ;
  return a;
}
int check(int mid) {
  int sum = 0;
  int res = 0;
  for (int i = 0; i < cnt; ++i) {
    if (arr[i] > mid) return 0;
    if (sum + arr[i] > mid) {
      res++;
      sum = 0;
    }
    sum += arr[i];
  }
  if (sum != 0) {
    res++;
    sum = 0;
  }
  return res <= k;
}
int main() {
  scanf("%d", &k);
  getchar();
  gets(str);
  int len = strlen(str);
  int j = 0;
  for (int i = 0; i < len; ++i) {
    j++;
    if (str[i] == ' ' || str[i] == '-') {
      arr[cnt++] = j;
      j = 0;
    }
  }
  arr[cnt++] = j;
  j = 0;
  int l = 0, r = len;
  int ans = 0;
  while (r - l >= 0) {
    int mid = (l + r) / 2;
    if (check(mid)) {
      r = mid - 1;
      ans = mid;
    } else {
      l = mid + 1;
    }
  }
  printf("%d\n", ans);
  return 0;
}
