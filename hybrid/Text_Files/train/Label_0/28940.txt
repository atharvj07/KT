#include <bits/stdc++.h>
using namespace std;
char s[200010];
vector<int> g[26];
int main() {
  int n, k;
  scanf("%d%d", &n, &k);
  scanf("%s", s);
  for (int i = 0; i < k; i++) g[s[i] - 'a'].push_back(i);
  for (int i = 0; i < 26; i++) sort(g[i].begin(), g[i].end());
  for (int i = 0; i < n; i++) {
    scanf("%s", s);
    k = strlen(s);
    long long res = 0;
    for (int j = 0; j < k; j++) {
      if (g[s[j] - 'a'].empty())
        res += k;
      else {
        int wsk = lower_bound(g[s[j] - 'a'].begin(), g[s[j] - 'a'].end(), j) -
                  g[s[j] - 'a'].begin();
        if (wsk && wsk < g[s[j] - 'a'].size())
          res += min(g[s[j] - 'a'][wsk] - j, j - g[s[j] - 'a'][wsk - 1]);
        else if (!wsk)
          res += g[s[j] - 'a'][wsk] - j;
        else
          res += j - g[s[j] - 'a'][wsk - 1];
      }
    }
    printf("%lld\n", res);
  }
  return 0;
}
