#include <bits/stdc++.h>
using namespace std;
struct Node {
  int len, link;
  int nxt[26];
  long long val;
};
struct Automaton {
  int sz, last;
  Node s[200100 * 10];
  void init() {
    sz = last = 0;
    s[0].len = 0;
    s[0].link = -1;
    s[0].val = 0;
    memset(s[0].nxt, 0, sizeof(s[0].nxt));
    ++sz;
  }
  void extend(int c, int cost) {
    int cur, p;
    if (s[last].nxt[c]) {
      cur = s[last].nxt[c];
      if (s[cur].len == s[last].len + 1) {
        s[cur].val += cost;
        last = cur;
        return;
      }
      int clone = sz++;
      s[clone] = s[cur];
      s[clone].len = s[last].len + 1;
      s[clone].val = cost;
      s[cur].link = clone;
      for (p = last; p != -1 && s[p].nxt[c] == cur; p = s[p].link)
        s[p].nxt[c] = clone;
      last = clone;
      return;
    }
    cur = sz++;
    s[cur].len = s[last].len + 1;
    s[cur].val = cost;
    for (p = last; p != -1 && !s[p].nxt[c]; p = s[p].link) s[p].nxt[c] = cur;
    if (p == -1)
      s[cur].link = 0;
    else {
      int q = s[p].nxt[c];
      if (s[p].len + 1 == s[q].len)
        s[cur].link = q;
      else {
        int clone = sz++;
        s[clone].len = s[p].len + 1;
        memcpy(s[clone].nxt, s[q].nxt, sizeof(s[q].nxt));
        s[clone].link = s[q].link;
        s[clone].val = 0;
        for (; p != -1 && s[p].nxt[c] == q; p = s[p].link) s[p].nxt[c] = clone;
        s[q].link = s[cur].link = clone;
      }
    }
    last = cur;
  }
  int cnt[10 * 200100], st[10 * 200100];
  long long solve(int len) {
    int i, j;
    for (j = 0; j <= len; j++) cnt[j] = 0;
    for (j = 0; j < sz; j++) cnt[s[j].len]++;
    for (j = 1; j <= len; j++) cnt[j] += cnt[j - 1];
    for (j = 0; j < sz; j++) st[cnt[s[j].len]--] = j;
    long long ret = 0;
    for (i = sz; i >= 1; i--) {
      int x = st[i];
      if (ret < s[x].val * s[x].len) ret = s[x].val * s[x].len;
      int p = s[x].link;
      if (p != -1) s[p].val += s[x].val;
    }
    return ret;
  }
} sam;
string str[200100];
int c[200100];
int main() {
  int N, i, len = 0;
  scanf("%d", &N);
  for (i = (0); i < (N); i++) cin >> str[i];
  for (i = (0); i < (N); i++) scanf("%d", &c[i]);
  sam.init();
  for (i = (0); i < (N); i++) {
    sam.last = 0;
    for (int j = 0; j < str[i].length(); j++) {
      sam.extend(str[i][j] - 'a', c[i]);
    }
    if (len < str[i].length()) len = str[i].length();
  }
  long long ans = sam.solve(len);
  cout << ans << endl;
  return 0;
}
