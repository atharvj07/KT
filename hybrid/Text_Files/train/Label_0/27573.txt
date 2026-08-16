#include <bits/stdc++.h>
using namespace std;
int l, r, p, ans, n, tot;
int prime[30];
int pr[35];
int tmp[35];
int f[3000005];
vector<int> cdt;
bool mark[3000005];
void dfs(int a, int b) {
  if (a > r || b > p) return;
  dfs(a, b + 1);
  if (mark[b]) return;
  if (a > r / b) return;
  cdt.push_back(a * b);
  dfs(a * b, b);
}
int main() {
  ios::sync_with_stdio(false);
  mark[0] = mark[1] = true;
  for (int i = 2; i <= 100; i++) {
    if (!mark[i]) prime[++n] = i;
    for (int j = 1; j <= n && i * prime[j] <= 100; j++) {
      mark[i * prime[j]] = true;
      if (i % prime[j] == 0) break;
    }
  }
  cin >> l >> r >> p;
  dfs(1, 0);
  cdt.push_back(1);
  sort(cdt.begin(), cdt.end());
  for (int i = 1; i < cdt.size(); i++) f[i] = 201;
  memset(mark, 0, sizeof(mark));
  for (int i = 2; i <= p; i++)
    for (int j = 0, k = 0; j < cdt.size(); j++) {
      if (cdt[j] > r / i) break;
      while (k < cdt.size() && (long long)cdt[j] * i > cdt[k]) k++;
      if (cdt[k] == (long long)cdt[j] * i && f[k] > f[j] + 1) {
        f[k] = f[j] + 1;
        if (!mark[k] && f[k] + i <= p) {
          mark[k] = true;
          ans += (cdt[k] >= l && cdt[k] <= r);
        }
      }
    }
  cout << ans << endl;
  return 0;
}
