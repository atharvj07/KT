#include <bits/stdc++.h>
using namespace std;
short fst[1 << 26];
char S[1001000], s[30];
int n, len, a[30], p[30], cnt[10100], y[10100], nxt[10100];
bool cmp(int x, int y) { return a[x] > a[y]; }
void add(int t, int i) {
  y[i] = t;
  nxt[i] = fst[t];
  fst[t] = i;
}
int main() {
  scanf("%s%d", S, &n);
  len = strlen(S);
  for (int i = 0; i < n; i++) {
    scanf("%s", s);
    int t = 0, q = strlen(s);
    for (int j = 0; j < q; j++) t |= (1 << (s[j] - 'a'));
    add(t, i + 1);
  }
  S[len] = 'a' + 26;
  for (int i = 0; i < 27; i++) a[i] = -1;
  for (int i = 0; i < len; i++) {
    if (S[i] == S[i + 1]) continue;
    int q = S[i + 1] - 'a', t = 0;
    a[S[i] - 'a'] = i;
    for (int i = 0; i < 27; i++) p[i] = i;
    sort(p, p + 27, cmp);
    for (int j = 0; j < 27; j++) {
      cnt[fst[t]]++;
      if (p[j] == q || a[p[j]] < 0) break;
      t |= (1 << p[j]);
    }
  }
  for (int i = n; i; i--) cnt[nxt[i]] = cnt[i];
  for (int i = 1; i <= n; i++) printf("%d\n", cnt[i]);
}
