#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1e9 + 7;
const int INF = 0x3f3f3f3f;
const long long LL_INF = 0x3f3f3f3f3f3f3f3f;
const double PI = acos(-1);
const double ERR = 1e-8;
const int MAXN = 1e7;
int a[2000], n;
int main(int argc, char const *argv[]) {
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  int l, r, m;
  scanf("%d", &m);
  int c = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {
      if (a[i] > a[j]) c++;
    }
  }
  while (m--) {
    scanf("%d%d", &l, &r);
    if (l < r) {
      int t = (r - l + 1);
      c += (t * (t - 1) / 2) % 2;
    }
    if (!(c % 2))
      printf("even\n");
    else
      printf("odd\n");
  }
  return 0;
}
