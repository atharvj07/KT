#include <bits/stdc++.h>
using namespace std;
int n, m, t;
const int su[] = {2,  3,  5,  7,  11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, -1};
const long long MODER[5] = {223092870ll, 2756205443ll, 907383479ll, 42600829ll,
                            97ll};
int b[100];
long long a[20000], c, ans;
char ss[100];
vector<long long> f[17][5];
void init() {
  for (int i = 2; i <= 16; i++) {
    int l = 1;
    for (int k = 1; k <= n; k *= i, l *= i + 1)
      ;
    for (int j = 0; j < 5; j++) f[i][j].resize(l, -1);
  }
}
int calc(int d, int p) {
  int x = 0, y = 0;
  for (int i = 0; i < t; i++) x = x * (d + 1) + b[i];
  if (f[d][p][x] != -1) return x;
  f[d][p][x] = 1;
  for (int i = 0; i < t; i++)
    if (b[i] == d) {
      for (int j = 0; j < d; j++)
        b[i] = j, f[d][p][x] = (f[d][p][x] * f[d][p][calc(d, p)]) % MODER[p];
      b[i] = d;
      return x;
    }
  for (int i = 0; i < t; i++) y = y * d + b[i];
  if (y < n) f[d][p][x] = a[y] % MODER[p];
  return x;
}
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; i++) scanf("%I64d", &a[i]);
  scanf("%d", &m);
  init();
  while (m--) {
    int d;
    long long c;
    scanf("%d%s%I64d", &d, ss, &c);
    t = 0;
    for (int j = 1; j <= n; t++, j *= d)
      ;
    int len = strlen(ss);
    for (int j = 0; j < t; j++)
      if (len - t + j >= 0)
        b[j] = ((ss[len - t + j]) == '?'
                    ? (d)
                    : ('0' <= (ss[len - t + j]) && (ss[len - t + j]) <= '9'
                           ? ss[len - t + j] - '0'
                           : ss[len - t + j] - 'A' + 10));
      else
        b[j] = 0;
    int j;
    for (int i = 0; i < 5; i++) {
      j = calc(d, i);
      ans = (f[d][i][j] + c) % MODER[i];
      for (j = 0; j < 25; j++)
        if (MODER[i] % su[j] == 0 && ans % su[j] == 0) break;
      if (j < 25) break;
    }
    printf("%d\n", su[j]);
  }
}
