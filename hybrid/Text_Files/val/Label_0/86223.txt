#include <bits/stdc++.h>
using namespace std;
const int maxn = 100005, maxl = 200005, maxsg = 60;
int n, f, SG, cnt, maxx;
int p[maxl], c[maxl], sg[maxl], A[maxn], B[maxn];
bitset<maxl> ok, have[maxsg];
void sieve(int n) {
  c[1] = 1;
  for (int i = 2; i <= n; i++) {
    if (c[i] == 0) p[++cnt] = i, ok[i] = 1;
    for (int j = 1; j <= cnt; j++) {
      if (i * p[j] > n) break;
      c[i * p[j]] = 1;
      if (c[i] == 0) ok[i * p[j]] = 1;
      if (i % p[j] == 0) break;
    }
  }
}
int main() {
  scanf("%d%d", &n, &f);
  for (int i = 1; i <= n; i++) {
    int x, y, z;
    scanf("%d%d%d", &x, &y, &z);
    A[i] = y - x - 1, B[i] = z - y - 1;
    maxx = max(maxx, max(A[i], B[i]));
  }
  sieve(maxx), ok[f] = 0, have[0] = ok;
  for (int i = 1; i <= maxx; i++) {
    while (have[sg[i]][i]) sg[i]++;
    have[sg[i]] |= (ok << i);
  }
  for (int i = 1; i <= n; i++) SG ^= sg[A[i]] ^ sg[B[i]];
  if (SG == 0)
    puts("Bob\nAlice");
  else
    puts("Alice\nBob");
  return 0;
}
