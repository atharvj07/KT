#include <bits/stdc++.h>
using namespace std;
map<int, int> a;
int n, G, S, Q, L, R, j;
map<int, int>::iterator k;
long long d[100005], t[100005];
void ins(int i, int L, int R) {
  if (L == R) return;
  map<int, int>::iterator j = a.lower_bound(L), k = a.upper_bound(R);
  int tmp = (--k)->second;
  a.erase(j, ++k);
  a[L] = i;
  a[R] = tmp;
}
int main() {
  scanf("%d%d%d", &n, &G, &S), S += G, a[0] = n + 1;
  for (int i = 1; i <= n + 1; i++) scanf("%I64d", &d[i]), d[i] += d[i - 1];
  for (int i = n; i; i--) {
    L = (G - d[i]) % S, R = (S - d[i]) % S, L < 0 ? L += S : 0,
    R < 0 ? R += S : 0;
    k = a.upper_bound((S - d[i] % S) % S), j = (--k)->second;
    if (j > n)
      t[i] = d[n + 1] - d[i];
    else
      t[i] = (d[j] - d[i] - 1) / S * S + S + t[j];
    if (L < R)
      ins(i, L, R);
    else
      ins(i, 0, R), ins(i, L, S);
  }
  scanf("%d", &Q);
  while (Q--)
    scanf("%d", &R),
        k = a.upper_bound(R % S), j = (--k)->second,
        printf("%I64d\n",
               j > n ? R + d[n + 1] : (R + d[j] - 1) / S * S + S + t[j]);
  return 0;
}
