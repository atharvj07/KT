#include <bits/stdc++.h>
using namespace std;
int T;
int n, m;
char s[200043];
int p[200043];
long long cnt[200043];
long long ans[43];
int main(int argc, char const *argv[]) {
  scanf("%d", &T);
  while (T--) {
    scanf("%d%d", &n, &m);
    scanf("%s", s);
    for (int i = 0; i < m; ++i) {
      scanf("%d", &p[i]);
      --p[i];
    }
    sort(p, p + m);
    memset(cnt, 0, sizeof(cnt));
    memset(ans, 0, sizeof(ans));
    int del = 0;
    int sci = 0;
    for (int i = 0; i < n; ++i) {
      cnt[i] += (long long)m - del;
      while (i == p[sci] && sci < m) {
        ++sci;
        ++del;
      }
    }
    for (int i = 0; i < n; ++i) ans[s[i] - 'a'] += cnt[i] + 1;
    for (int i = 0; i < 26; ++i) printf("%d ", ans[i]);
    printf("\n");
  }
  return 0;
}
