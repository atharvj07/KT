#include <bits/stdc++.h>
using namespace std;
const int inf = 1e9 + 7;
const int mod = 1e9 + 7;
const int maxn = 1e5 + 7;
const int maxmsk = (1 << 17) + 7;
int n, p, num[maxn], ok[27][27];
int bad[maxmsk], met[27], sum[27];
bool hve[27];
string s;
void init() {
  scanf("%d%d", &n, &p);
  cin >> s;
  for (int i = 0; i < n; i++) num[i] = s[i] - 'a', sum[num[i]]++;
  for (int i = 0; i < p; i++) {
    for (int j = 0; j < p; j++) scanf("%d", ok[i] + j);
  }
}
void solve() {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < p; j++) {
      if (!hve[j]) continue;
      if ((met[j] >> (num[i])) & 1) continue;
      if (ok[num[i]][j]) continue;
      bad[met[j]]++;
      bad[met[j] | (1 << j)]--;
      bad[met[j] | (1 << num[i])]--;
      bad[met[j] | (1 << j) | (1 << num[i])]++;
    }
    hve[num[i]] = true;
    for (int j = 0; j < p; j++) met[j] |= (1 << num[i]);
    met[num[i]] = 0;
  }
  for (int i = 0; i < p; i++) {
    for (int j = 0; j < (1 << p); j++) {
      if ((j >> i) & 1) bad[j] += bad[j ^ (1 << i)];
    }
  }
  int ans = n;
  for (int i = 1; i < (1 << p); i++) {
    if (bad[i]) continue;
    bool isbad = true;
    for (int j = 0; j < p; j++) {
      if ((i >> j) & 1) {
        if (!bad[i ^ (1 << j)]) {
          isbad = false;
          break;
        }
      }
    }
    if (isbad) {
      bad[i] = 1;
      continue;
    }
    int res = 0;
    for (int j = 0; j < p; j++) {
      if (!((i >> j) & 1)) res += sum[j];
    }
    ans = min(ans, res);
  }
  printf("%d\n", ans);
}
int main() {
  init();
  solve();
  return 0;
}
