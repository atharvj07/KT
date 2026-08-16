#include <bits/stdc++.h>
using namespace std;
const double PI = acos(-1.0);
const int maxn = 1e5 + 5;
const int Inf = 1e9 + 7;
int n;
int a[maxn];
int isprime[maxn];
int prime[maxn];
int pnum = 0;
int ans[maxn];
void elect_Prime() {
  memset(isprime, 1, sizeof(isprime));
  for (int i = 2; i < 1e5 + 2; i++) {
    if (isprime[i]) prime[pnum++] = i;
    for (int j = 0; j < pnum && i * prime[j] < 1e5 + 2; j++) {
      isprime[i * prime[j]] = 0;
      if (i % prime[j] == 0) break;
    }
  }
}
int main() {
  while (scanf("%d", &n) != EOF) {
    int x;
    memset(ans, 0, sizeof(ans));
    for (int i = 1; i <= n; i++) {
      scanf("%d", &x);
      for (int j = 1; j * j <= x; j++) {
        if (x % j == 0) {
          ans[j] += 1;
          if (j * j != x) {
            ans[x / j] += 1;
          }
        }
      }
    }
    int num = 1;
    for (int i = 2; i < maxn; i++) {
      num = max(num, ans[i]);
    }
    printf("%d\n", num);
  }
  return 0;
}
