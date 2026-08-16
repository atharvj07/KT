#include <bits/stdc++.h>
char s[100010], t[100010];
int next[100010], occ[100010], n = 0, lens, lent;
long long f[100010], g[100010];
int main() {
  scanf("%s%s", s, t), lens = strlen(s), lent = strlen(t);
  next[0] = next[1] = 0;
  for (int i = 1, j; i < lent; i++) {
    j = next[i];
    while (j && t[i] != t[j]) j = next[j];
    next[i + 1] = (t[i] == t[j] ? j + 1 : 0);
  }
  for (int i = 0, cur = -1; i < lens; i++) {
    if (cur == -1 && s[i] == t[0])
      cur = 0;
    else {
      while (cur >= 0 && s[i] != t[cur + 1]) cur = next[cur + 1] - 1;
      if (cur == -1 && s[i] == t[0])
        cur = 0;
      else if (s[i] == t[cur + 1])
        cur++;
    }
    if (cur == lent - 1) occ[n++] = i - lent + 2, cur = next[cur + 1] - 1;
  }
  f[0] = g[0] = 1;
  for (int i = 1, last = 0, cur = 0; i <= lens; i++) {
    if (cur < n && occ[cur] + lent - 1 == i) last = i - lent + 1, cur++;
    f[i] = (f[i - 1] + (last ? g[last - 1] : 0)) % 1000000007;
    g[i] = (g[i - 1] + f[i]) % 1000000007;
  }
  printf("%I64d\n", ((f[lens] - 1) % 1000000007 + 1000000007) % 1000000007);
  return 0;
}
