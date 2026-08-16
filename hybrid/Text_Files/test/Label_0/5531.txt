#include <bits/stdc++.h>
using namespace std;
const int INF = (1 << 30) - 1;
const long long lINF = (1LL << 62) - 1;
const double dINF = 1e40;
const int MAXN = 205, MAX_NODE = MAXN * MAXN, MAXM = 20, MAXV = 505;
struct Trie {
  struct TrieNode {
    TrieNode *nxt[MAXM], *fail;
    int sum;
  } buf[MAX_NODE], *top, *root;
  TrieNode *new_node() { return top++; }
  Trie() {
    memset(buf, 0, sizeof(buf));
    top = buf;
    root = new_node();
  }
  int get_nxt(int id, int c) { return buf[id].nxt[c] - buf; }
  void insert(const vector<int> &str, int val) {
    int len = str.size();
    auto x = root;
    for (int i = 0; i < len; i++) {
      int c = str[i];
      if (x->nxt[c] == NULL) x->nxt[c] = new_node();
      x = x->nxt[c];
    }
    x->sum += val;
  }
  void solve() {
    queue<TrieNode *> que;
    que.push(root);
    root->fail = NULL;
    while (!que.empty()) {
      auto x = que.front();
      que.pop();
      for (int c = 0; c < MAXM; c++)
        if (x->nxt[c]) {
          que.push(x->nxt[c]);
          x->nxt[c]->fail = (x->fail == NULL ? root : x->fail->nxt[c]);
        } else
          x->nxt[c] = (x->fail == NULL ? root : x->fail->nxt[c]);
      if (x->fail) x->sum += x->fail->sum;
    }
  }
} trie;
typedef int dp_arr[MAX_NODE][MAXV];
dp_arr dp[2];
vector<int> read_vec() {
  int len;
  scanf("%d", &len);
  vector<int> res(len);
  for (int i = 0; i < len; i++) scanf("%d", &res[i]);
  return res;
}
const int mod = 1000000007;
void add(int &a, int b) { a = (a + b) % mod; }
int solve(const vector<int> &s, int m, int lm) {
  int len = s.size();
  int lap = 0;
  memset(dp[lap], 0, sizeof(dp[lap]));
  int tp = 0, tk = 0, sz = trie.top - trie.buf;
  for (int i = 0; i < len; i++, lap ^= 1) {
    dp_arr &cur = dp[lap ^ 1], &pre = dp[lap];
    memset(cur, 0, sizeof(cur));
    for (int j = 0; j < sz; j++)
      for (int k = 0; k <= lm; k++)
        if (pre[j][k]) {
          for (int c = 0; c < m; c++) {
            int nj = trie.get_nxt(j, c), nk = k + trie.buf[nj].sum;
            if (nk <= lm) add(cur[nj][nk], pre[j][k]);
          }
        }
    for (int c = i == 0 ? 1 : 0; c < s[i]; c++) {
      int nj = trie.get_nxt(tp, c), nk = tk + trie.buf[nj].sum;
      if (nk <= lm) add(cur[nj][nk], 1);
    }
    if (i > 0) {
      for (int c = 1; c < m; c++) {
        int nj = trie.get_nxt(0, c), nk = trie.buf[nj].sum;
        if (nk <= lm) add(cur[nj][nk], 1);
      }
    }
    tp = trie.get_nxt(tp, s[i]);
    tk += trie.buf[tp].sum;
  }
  int ans = 0;
  for (int j = 0; j < sz; j++)
    for (int k = 0; k <= lm; k++) add(ans, dp[lap][j][k]);
  return ans;
}
int main() {
  int n, m, lm;
  scanf("%d%d%d", &n, &m, &lm);
  vector<int> vl = read_vec();
  vector<int> vr = read_vec();
  for (int t = 0; t < n; t++) {
    vector<int> s = read_vec();
    int val;
    scanf("%d", &val);
    trie.insert(s, val);
  }
  trie.solve();
  int ans = solve(vr, m, lm) - solve(vl, m, lm);
  auto x = trie.root;
  int sk = 0;
  for (int i = 0; i < vr.size(); i++) {
    x = x->nxt[vr[i]];
    sk += x->sum;
  }
  if (sk <= lm) ans++;
  if (ans < 0) ans += mod;
  printf("%d\n", ans);
  return 0;
}
