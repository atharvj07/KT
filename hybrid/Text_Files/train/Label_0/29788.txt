#include <bits/stdc++.h>
#pragma GCC optimize(2)
#pragma G++ optimize(2)
using namespace std;
const int MAX_N = 2e5 + 5;
struct AC_Automation {
  int nxt[MAX_N][26], ed[MAX_N], fail[MAX_N];
  int root, L;
  int num[MAX_N];
  int new_node() {
    ed[++L] = 0;
    for (register int i = 0; i <= 25; ++i) nxt[L][i] = -1;
    return L;
  }
  void init() {
    L = 0;
    root = new_node();
  }
  void insert(char *s) {
    int len = strlen(s + 1);
    int now = root;
    for (register int i = 1; i <= len; ++i) {
      if (nxt[now][s[i] - 'a'] == -1) nxt[now][s[i] - 'a'] = new_node();
      now = nxt[now][s[i] - 'a'];
    }
    ed[now]++;
  }
  void get_fail() {
    queue<int> Q;
    fail[root] = root;
    for (register int i = 0; i <= 25; ++i) {
      if (nxt[root][i] == -1)
        nxt[root][i] = root;
      else {
        fail[nxt[root][i]] = root;
        Q.push(nxt[root][i]);
      }
    }
    while (!Q.empty()) {
      int now = Q.front();
      Q.pop();
      for (register int i = 0; i <= 25; ++i) {
        if (nxt[now][i] == -1)
          nxt[now][i] = nxt[fail[now]][i];
        else {
          fail[nxt[now][i]] = nxt[fail[now]][i];
          Q.push(nxt[now][i]);
          ed[nxt[now][i]] += ed[fail[nxt[now][i]]];
        }
      }
    }
  }
  void find(char *s) {
    int now = root, len = strlen(s + 1);
    for (register int i = 1; i <= len; ++i) {
      now = nxt[now][s[i] - 'a'];
      num[i] = ed[now];
    }
  }
} ac1, ac2;
char s[MAX_N], t[MAX_N];
int main() {
  scanf("%s", s + 1);
  int n;
  scanf("%d", &n);
  ac1.init(), ac2.init();
  for (register int i = 1; i <= n; ++i) {
    scanf("%s", t + 1);
    ac1.insert(t);
    int len = strlen(t + 1);
    reverse(t + 1, t + 1 + len);
    ac2.insert(t);
  }
  ac1.get_fail(), ac2.get_fail();
  ac1.find(s);
  int len = strlen(s + 1);
  reverse(s + 1, s + 1 + len);
  ac2.find(s);
  reverse(ac2.num + 1, ac2.num + 1 + len);
  long long ans = 0;
  for (register int i = 1; i <= len; ++i)
    ans += 1ll * ac1.num[i] * ac2.num[i + 1];
  printf("%lld\n", ans);
  return 0;
}
