#include <bits/stdc++.h>
using namespace std;
int mod = 998244353;
const int M = 1e6 + 10;
const int N = 5e5 + 10;
inline long long read() {
  long long b = 1, sum = 0;
  char c = getchar();
  while (!isdigit(c)) {
    if (c == '-') b = -1;
    c = getchar();
  }
  while (isdigit(c)) {
    sum = sum * 10 + c - '0';
    c = getchar();
  }
  return b * sum;
}
int n, m, k, T;
int len, ans;
int a[N], sum[N];
int pcnt, p[N], d[N];
bool vis[N + 10];
void sieve() {
  int i, j;
  for (i = 2; i <= n; i++) {
    if (!vis[i]) {
      p[++pcnt] = i;
      d[i] = 1;
      for (j = 2 * i; j <= n; j += i) {
        vis[j] = 1;
        d[j] = max(d[j], j / i);
      }
    }
  }
}
int main() {
  int i, j;
  n = read();
  sieve();
  d[1] = 1;
  sort(d + 1, d + 1 + n);
  for (i = 2; i <= n; i++) {
    printf("%d ", d[i]);
  }
  return 0;
}
