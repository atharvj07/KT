#include <bits/stdc++.h>
using namespace std;
const long long mod = 998244353;
const int Maxn = 1e5 + 5;
int head[Maxn], Next[Maxn], ver[Maxn];
int tot = 0;
void add(int x, int y) {
  Next[++tot] = head[x];
  head[x] = tot;
  ver[tot] = y;
}
int head1[Maxn], Next1[Maxn], ver1[Maxn];
int tot1 = 0;
void add1(int x, int y) {
  Next1[++tot1] = head1[x];
  head1[x] = tot1;
  ver1[tot1] = y;
}
int a[Maxn];
int ru[Maxn];
int id[Maxn];
queue<int> qm, qco;
int main() {
  int n, m;
  scanf("%d %d", &n, &m);
  for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
  int x, y;
  for (int i = 1; i <= m; i++) {
    scanf("%d %d", &y, &x);
    x++;
    y++;
    ru[y]++;
    add(x, y);
  }
  for (int i = 1; i <= n; i++) {
    if (ru[i] == 0) {
      if (a[i])
        qco.push(i);
      else
        qm.push(i);
    }
  }
  int ans = 0;
  while (qco.size() || qm.size()) {
    while (qm.size()) {
      x = qm.front();
      qm.pop();
      for (int i = head[x]; i; i = Next[i]) {
        y = ver[i];
        ru[y]--;
        if (ru[y] == 0) {
          if (!a[y])
            qm.push(y);
          else
            qco.push(y);
        }
      }
    }
    if (!qco.empty()) ans++;
    while (qco.size()) {
      x = qco.front();
      qco.pop();
      for (int i = head[x]; i; i = Next[i]) {
        y = ver[i];
        ru[y]--;
        if (ru[y] == 0) {
          if (!a[y])
            qm.push(y);
          else
            qco.push(y);
        }
      }
    }
  }
  cout << ans << endl;
}
