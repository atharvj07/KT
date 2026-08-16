#include <bits/stdc++.h>
using namespace std;
const int maxn = 2e3 + 15;
const int mod = 998244353;
const int inf = 0x3f3f3f3f;
int n;
int main() {
  int T;
  scanf("%d", &T);
  while (T--) {
    scanf("%d", &n);
    int la = 0, lb = 0;
    bool f = 1;
    for (int i = 0, a, b; i < n; i++) {
      scanf("%d%d", &a, &b);
      if (a < la || b < lb) f = 0;
      if (a - la < b - lb) f = 0;
      la = a;
      lb = b;
    }
    if (f)
      puts("YES");
    else
      puts("NO");
  }
  return 0;
}
