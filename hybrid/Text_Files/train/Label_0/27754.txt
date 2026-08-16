#include <bits/stdc++.h>
using namespace std;
const int INF = 1e9 + 7;
int read() {
  int x = 0, f = 1, ch = getchar();
  while (!isdigit(ch)) {
    if (ch == '-') f = -1;
    ch = getchar();
  }
  while (isdigit(ch)) x = (x << 1) + (x << 3) + ch - '0', ch = getchar();
  return x * f;
}
int n, L, p[100005], a[100005], pre[100005], nxt[100005], x[100005];
bool cmp(int a, int b) { return p[a] < p[b]; }
set<pair<int, int> > st;
int dis(int i, int j) {
  if (i == j) return INF;
  register int d = (p[j] - p[i] + L) % L;
  if (i > j) d = (d + a[j]) % L;
  if (d <= a[i]) return 1;
  if (a[i] <= a[j]) return INF;
  return (d - a[j] - 1) / (a[i] - a[j]) + 1;
}
signed main() {
  n = read(), L = read();
  for (register int i = 1; i <= n; i++) {
    p[i] = read(), a[i] = read(), x[i] = i;
  }
  sort(x + 1, x + 1 + n, cmp);
  pre[x[1]] = x[n];
  for (int i = 1; i <= n; i++) {
    if (i > 1) pre[x[i]] = x[i - 1];
    nxt[pre[x[i]]] = x[i];
  }
  for (int i = 1; i <= n; i++) st.insert(make_pair(dis(i, nxt[i]), i));
  set<pair<int, int> >::iterator it;
  while (st.size()) {
    it = st.begin();
    register int i = it->second, d = it->first;
    if (d == INF) break;
    st.erase(it);
    st.erase(make_pair(dis(nxt[i], nxt[nxt[i]]), nxt[i]));
    st.erase(make_pair(dis(pre[i], i), pre[i]));
    p[i] = (p[i] + d - 1) % L + 1;
    a[i]--;
    nxt[i] = nxt[nxt[i]];
    pre[nxt[i]] = i;
    st.insert(make_pair(dis(pre[i], i), pre[i]));
    st.insert(make_pair(dis(i, nxt[i]), i));
  }
  printf("%d\n", st.size());
  while (st.size()) {
    it = st.begin();
    printf("%d ", it->second);
    st.erase(it);
  }
  return 0;
}
