#include <bits/stdc++.h>
using namespace std;
const int mod = 998244353;
const int maxc = 1000010;
const int base = 1e6 + 11;
const int maxk = 100010;
const int mod1 = 1145141;
const int mod2 = 1e9 + 9;
int ans = 0;
int inv[maxc], ijc[maxc], jc[maxc], pw1[maxk], pw2[maxk];
int cnt[maxc], mx = 0, v1, v2;
int k, a[maxk], cur_a[maxk];
set<pair<int, int> > st;
int binom(int n, int m) {
  if (m > n) return 0;
  return 1LL * jc[n] * ijc[m] % mod * ijc[n - m] % mod;
}
struct CMP {
  bool operator()(int x, int y) { return cur_a[x] > cur_a[y]; }
};
priority_queue<int, vector<int>, CMP> pq;
int main() {
  scanf("%d", &k);
  for (int i = 1; i <= k; i++) scanf("%d", &a[i]);
  pw1[0] = pw2[0] = 1;
  for (int i = 1; i <= k; i++)
    pw1[i] = 1LL * pw1[i - 1] * base % mod1,
    pw2[i] = 1LL * pw2[i - 1] * base % mod2;
  inv[1] = 1;
  for (int i = 2; i <= 1000000; i++)
    inv[i] = mod - 1LL * (mod / i) * inv[mod % i] % mod;
  jc[0] = ijc[0] = 1;
  for (int i = 1; i <= 1000000; i++)
    jc[i] = 1LL * jc[i - 1] * i % mod, ijc[i] = 1LL * ijc[i - 1] * inv[i] % mod;
  for (int i = 1; i <= k; i++) cur_a[i] = a[i];
  for (int i = 1; i <= k; i++) {
    v1 = (1LL * cur_a[i] * pw1[i] % mod1 + v1) % mod1;
    v2 = (1LL * cur_a[i] * pw2[i] % mod2 + v2) % mod2;
  }
  for (int i = 1; i <= k; i++) pq.push(i);
  int sum1 = 0, sum2 = 0;
  for (int i = 1; i <= k; i++)
    sum1 = (sum1 + mod1 - pw1[i]) % mod1, sum2 = (sum2 + mod2 - pw2[i]) % mod2;
  while (1) {
    cnt[mx + 1] = cnt[mx];
    while (cur_a[pq.top()] - mx - 1 < 0) {
      int t = pq.top();
      pq.pop();
      ++cnt[mx + 1];
      cur_a[t] += k;
      v1 = (v1 + 1LL * k * pw1[t] % mod1) % mod1;
      v2 = (v2 + 1LL * k * pw2[t] % mod2) % mod2;
      pq.push(t);
    }
    v1 = (v1 + sum1) % mod1;
    v2 = (v2 + sum2) % mod2;
    if (st.count(pair<int, int>(v1, v2))) break;
    if (cnt[mx + 1] > mx + 1) break;
    st.insert(pair<int, int>(v1, v2));
    ++mx;
  }
  for (int i = 0; i < k; i++) {
    if (i > mx) break;
    int t = (mx - i) / k;
    int x = i + t * k;
    int c = x - cnt[x];
    ans = (ans + binom(c + k - 1, k - 1)) % mod;
  }
  printf("%d\n", ans);
  return 0;
}
