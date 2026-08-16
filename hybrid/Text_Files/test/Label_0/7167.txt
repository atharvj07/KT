#include <bits/stdc++.h>
using namespace std;
const int N = (int)1e6 + 10, mod = (int)1e9 + 7;
int q, last, sz;
char s[N];
struct state {
  int len, link, next[26], cnt;
};
vector<state> st;
vector<bool> vis;
vector<int> adj[2 * N];
void sa_init() {
  st.resize(2 * N);
  vis.resize(2 * N);
  st[0].link = -1;
  st[0].len = 0;
  last = 0;
  sz = 1;
}
void sa_extend(char ch) {
  int c = ch - 'a';
  int cur = sz++;
  st[cur].len = st[last].len + 1;
  int p = last;
  while (p != -1 && !st[p].next[c]) {
    st[p].next[c] = cur;
    p = st[p].link;
  }
  if (p == -1)
    st[cur].link = 0;
  else {
    int q = st[p].next[c];
    if (st[q].len == st[p].len + 1)
      st[cur].link = q;
    else {
      int clone = sz++;
      st[clone] = st[q];
      st[clone].cnt = 0;
      st[clone].len = st[p].len + 1;
      while (p != -1 && st[p].next[c] == q) {
        st[p].next[c] = clone;
        p = st[p].link;
      }
      st[q].link = st[cur].link = clone;
    }
  }
  last = cur;
  st[cur].cnt = 1;
}
void dfs(int u) {
  for (int v : adj[u]) {
    dfs(v);
    st[u].cnt += st[v].cnt;
  }
}
int main() {
  sa_init();
  char x;
  while ((x = getchar()) != '\n') sa_extend(x);
  for (int i = 1; i < sz; i++) adj[st[i].link].push_back(i);
  dfs(0);
  scanf("%d", &q);
  for (int i = 0; i < q; i++) {
    scanf("%s", &s);
    vector<int> v;
    int n = strlen(s);
    int l = 0, len = 0, u = 0, ans = 0;
    for (int j = 0; j < n; j++) {
      while (len < n) {
        int c = s[l] - 'a';
        if (!st[u].next[c]) break;
        u = st[u].next[c];
        l++, len++;
        if (l == n) l = 0;
      }
      if (len == n) {
        if (!vis[u]) ans += st[u].cnt;
        vis[u] = 1;
        v.push_back(u);
      }
      if (u) {
        if (st[st[u].link].len == len - 1) {
          u = st[u].link;
        }
        len--;
      } else
        l = (l + 1) % n;
    }
    for (int a : v) vis[a] = 0;
    printf("%d\n", ans);
  }
  return 0;
}
