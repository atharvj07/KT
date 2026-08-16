#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5, P = 1e9 + 7;
int n, m, Q, fc[N], ifc[N], pw[N], len[N];
char s[N];
bool vis[N];
vector<int> f[N];
int inv(int x) { return x == 1 ? x : 1LL * (P - P / x) * inv(P % x) % P; }
int C(int n, int m) {
  return n < m ? 0 : 1LL * fc[n] * ifc[n - m] % P * ifc[m] % P;
}
int main() {
  pw[0] = fc[0] = 1;
  for (int i = 1; i <= N - 5; ++i)
    pw[i] = 25LL * pw[i - 1] % P, fc[i] = 1LL * i * fc[i - 1] % P;
  ifc[N - 5] = inv(fc[N - 5]);
  for (int i = N - 6; ~i; --i) ifc[i] = 1LL * (i + 1) * ifc[i + 1] % P;
  for (scanf("%d%s", &Q, s), m = strlen(s); Q--;) {
    int op;
    scanf("%d", &op);
    if (op == 1)
      scanf("%s", s), m = strlen(s);
    else {
      scanf("%d", &n);
      if (!vis[m]) {
        f[m].push_back(0), vis[m] = 1;
        for (int i = 1; i <= N - 5; ++i)
          f[m].push_back((1LL * C(i - 1, m - 1) * (i < m ? 0 : pw[i - m]) % P +
                          26LL * f[m][i - 1] % P) %
                         P);
      }
      printf("%d\n", f[m][n]);
    }
  }
  return 0;
}
