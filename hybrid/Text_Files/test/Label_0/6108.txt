#include <bits/stdc++.h>
using namespace std;
const int N = 3000 + 5, H = 137, P = 1e9 + 7;
int st[N], en[N], sz[N], power[N] = {1};
int h1[N][N], h2[N][N];
string w1[N], w2[N];
int get_hash(int st, int en, int h[N]) {
  return (h[en] - 1LL * h[st] * power[en - st] % P + P) % P;
}
int main() {
  ios_base ::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) cin >> w1[i];
  for (int i = 0; i < n; i++) cin >> w2[i];
  int u;
  for (int i = 1; i < N; i++) power[i] = 1LL * power[i - 1] * H % P;
  for (int i = 0; i < n; i++) {
    st[i] = sz[i] = w1[i].size(), en[i] = -1;
    for (int j = 0; j < sz[i]; j++) {
      if (w1[i][j] != w2[i][j]) st[i] = min(st[i], j), en[i] = j;
      h1[i][j + 1] = (1LL * h1[i][j] * H + w1[i][j]) % P,
                h2[i][j + 1] = (1LL * h2[i][j] * H + w2[i][j]) % P;
    }
    if (~en[i]) u = i;
  }
  int L = st[u], R = sz[u] - en[u] - 1;
  for (int i = 0; i < n; i++)
    if (~en[i]) {
      L = min(L, st[i]), R = min(R, sz[i] - en[i] - 1);
      while (L && get_hash(st[i] - L, st[i], h1[i]) ^
                      get_hash(st[u] - L, st[u], h1[u]))
        L--;
      while (R && get_hash(en[i], en[i] + R + 1, h1[i]) ^
                      get_hash(en[u], en[u] + R + 1, h1[u]))
        R--;
    }
  int hs = get_hash(st[u] - L, en[u] + R + 1, h1[u]),
      ht = get_hash(st[u] - L, en[u] + R + 1, h2[u]);
  string s = w1[u].substr(st[u] - L, en[u] - st[u] + L + R + 1),
         t = w2[u].substr(st[u] - L, en[u] - st[u] + L + R + 1);
  for (int i = 0; i < n; i++) {
    bool ok = (h1[i][sz[i]] == h2[i][sz[i]]);
    for (int st = 0, en = s.size(); en <= sz[i]; st++, en++)
      if (get_hash(st, en, h1[i]) == hs) {
        ok = !(h1[i][st] ^ h2[i][st] || get_hash(st, en, h2[i]) ^ ht ||
               get_hash(en, sz[i], h1[i]) ^ get_hash(en, sz[i], h2[i]));
        break;
      }
    if (!ok) return cout << "NO\n", 0;
  }
  cout << "YES\n" << s << endl << t << endl;
  return 0;
}
