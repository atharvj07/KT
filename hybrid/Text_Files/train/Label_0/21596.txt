#include <bits/stdc++.h>
void RI() {}
template <typename... T>
void RI(int &x, T &...tail) {
  scanf("%d", &x);
  RI(tail...);
}
using namespace std;
const int maxn = 200005;
int n;
int ar[maxn];
void read() {
  RI(n);
  for (int i = 1; i <= n; i++) RI(ar[i]);
}
int l[maxn], r[maxn];
void build() {
  vector<pair<int, int> > v(1, make_pair(0, 0));
  for (int i = 1; i <= n; i++) {
    while (v.back().first >= ar[i]) v.pop_back();
    l[i] = v.back().second;
    v.push_back(make_pair(ar[i], i));
  }
  v = vector<pair<int, int> >(1, make_pair(0, n + 1));
  for (int i = n; i >= 1; i--) {
    while (v.back().first >= ar[i]) v.pop_back();
    r[i] = v.back().second;
    v.push_back(make_pair(ar[i], i));
  }
}
int ans[maxn];
void sol() {
  for (int i = 1; i <= n; i++)
    ans[r[i] - l[i] - 1] = max(ans[r[i] - l[i] - 1], ar[i]);
  for (int i = n - 1; i >= 1; i--) ans[i] = max(ans[i], ans[i + 1]);
  for (int i = 1; i <= n; i++) printf("%d%c", ans[i], " \n"[i == n]);
}
int main() {
  read();
  build();
  sol();
}
