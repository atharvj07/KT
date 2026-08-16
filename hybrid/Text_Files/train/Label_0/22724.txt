#include <bits/stdc++.h>
using namespace std;
const long double eps = 1e-5;
const long double PI = acos(-1);
const int INF = (int)1e9;
const long long INFF = (long long)1e18;
const int mod = (int)1e9 + 7;
const int MXN = (int)1e5 + 7;
char s1[MXN], s2[MXN];
int fail[MXN];
long long hh[MXN][27], bs[MXN][27], bs2[MXN][5];
long long val1[MXN][27], val2[MXN][27];
long long val3[MXN][7], val4[MXN][7];
int MOD[5] = {1010102101, 1010101333, 999991921, mod, 1076767633};
mt19937 rng(0x5EED);
long long randint(long long lb = 0, long long ub = INFF) {
  return uniform_int_distribution<long long>(lb, ub)(rng);
}
int l1, l2;
vector<int> st;
void build() {
  int l = strlen(s2 + 1);
  fail[1] = 0;
  int pos = 0;
  for (int i = 2; i <= l; ++i) {
    while (pos != 0 && s2[i] != s2[pos + 1]) pos = fail[pos];
    if (s2[i] == s2[pos + 1]) pos++;
    fail[i] = pos;
    if (fail[i]) st.push_back(i - fail[i]);
  }
  sort(begin(st), end(st));
  return;
}
bool check(int ll, int len) {
  if (ll + len - 1 > l1) return 0;
  for (int j = 0; j < 5; ++j) {
    long long v1 = (val3[ll + len - 1][j] -
                    val3[ll - 1][j] * bs2[len][j] % MOD[j] + MOD[j]) %
                   MOD[j];
    long long v2 = val4[len][j];
    if (v1 != v2) return 0;
  }
  return 1;
}
int main(void) {
  scanf("%s %s", s1 + 1, s2 + 1);
  l1 = strlen(s1 + 1);
  l2 = strlen(s2 + 1);
  build();
  for (int j = 0; j < 5; ++j) {
    bs2[0][j] = 1;
    bs2[1][j] = 26;
    for (int i = 2; i < MXN; ++i) bs2[i][j] = bs2[i - 1][j] * 26 % MOD[j];
  }
  for (int j = 0; j < 20; ++j) {
    for (int i = 0; i < 26; ++i) hh[i][j] = randint();
    bs[0][j] = 1;
    bs[1][j] = randint();
    for (int i = 2; i < MXN; ++i) bs[i][j] = bs[i - 1][j] * bs[1][j];
    for (int i = 1; i < l1 + 1; ++i) {
      val1[i][j] = (val1[i - 1][j] * bs[1][j] + hh[s1[i] - 'a'][j]);
    }
    for (int i = 1; i < l2 + 1; ++i) {
      val2[i][j] = (val2[i - 1][j] * bs[1][j] + hh[s2[i] - 'a'][j]);
    }
  }
  for (int j = 0; j < 5; ++j) {
    for (int i = 1; i < l1 + 1; ++i) {
      val3[i][j] = (val3[i - 1][j] * 26 + s1[i] - 'a') % MOD[j];
    }
    for (int i = 1; i < l2 + 1; ++i) {
      val4[i][j] = (val4[i - 1][j] * 26 + s2[i] - 'a') % MOD[j];
    }
  }
  long long ans = l1 * 1ll * l2;
  for (int i = 2; i < l1 + 1; ++i) {
    int ll = 0, rr = (int)(st).size() - 1, ok = -1;
    while (ll <= rr) {
      int mid = (ll + rr) >> 1;
      if (check(i, st[mid]))
        ll = mid + 1, ok = mid;
      else
        rr = mid - 1;
    }
    ans -= (ok + 1);
  }
  printf("%lld\n", ans);
  return 0;
}
