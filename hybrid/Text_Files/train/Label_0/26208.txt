#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 200;
const int M = 1e5 + 100;
template <class Ruby_Rose>
inline void read(Ruby_Rose &x) {
  x = 0;
  char ch = getchar(), w = 0;
  while (!isdigit(ch)) w = (ch == '-'), ch = getchar();
  while (isdigit(ch)) x = (x << 1) + (x << 3) + (ch ^ 48), ch = getchar();
  x = w ? -x : x;
}
int n, m, p, q[M];
long long dis[N], val[M], f[M][2], sum[N];
inline int check(int a, int b, int c, int d) {
  return 1.0 * (f[c][d] + sum[c] - f[b][d] - sum[b]) / (c - b) <=
         1.0 * (f[b][d] + sum[b] - f[a][d] - sum[a]) / (b - a);
}
int main() {
  read(n), read(m), read(p);
  for (register int i = 2; i <= n; i++) read(dis[i]), dis[i] += dis[i - 1];
  for (register int i = 1, h; i <= m; i++)
    read(h), read(val[i]), val[i] -= dis[h];
  sort(val + 1, val + 1 + m);
  for (register int i = 1; i <= m; i++) sum[i] = sum[i - 1] + val[i];
  f[0][0] = 0;
  for (register int i = 1; i <= m; i++) f[i][0] = 1e15;
  for (register int j = 1; j <= p; j++) {
    int st = 1, ed = 0;
    for (register int i = 1; i <= m; i++) {
      while (st < ed && check(q[ed - 1], q[ed], i - 1, j & 1 ^ 1)) ed--;
      q[++ed] = i - 1;
      while (st < ed && 1.0 *
                                (f[q[st + 1]][j & 1 ^ 1] + sum[q[st + 1]] -
                                 f[q[st]][j & 1 ^ 1] - sum[q[st]]) /
                                (q[st + 1] - q[st]) <=
                            1.0 * val[i])
        st++;
      f[i][j & 1] =
          f[q[st]][j & 1 ^ 1] + (i - q[st]) * val[i] - (sum[i] - sum[q[st]]);
    }
  }
  cout << f[m][p & 1] << endl;
  return 0;
}
