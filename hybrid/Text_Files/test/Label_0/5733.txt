#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7, N = 1e5 + 10;
int n, m, f[N];
int main() {
  f[1] = 1, f[2] = 2;
  for (int i = 3; i < N; ++i) f[i] = (f[i - 1] + f[i - 2]) % mod;
  scanf("%d%d", &n, &m);
  printf("%d\n", 2ll * (f[n] + f[m] - 1) % mod);
  return 0;
}
