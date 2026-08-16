#include <bits/stdc++.h>
using namespace std;
using lli = long long;
using lld = long double;
using ulli = unsigned long long int;
using pll = pair<lli, lli>;
using ttt = pair<lli, pll>;
using vttt = vector<ttt>;
using vll = vector<pll>;
using vl = vector<lli>;
using vi = vector<int>;
using vvi = vector<vector<int>>;
using cd = complex<lld>;
const double PI = acos(-1);
inline lli mpow(lli a, lli b, lli m = 1000000007) {
  lli ans = 1;
  while (b) {
    if (b & 1) ans = (ans * a) % m;
    a = (a * a) % m;
    b /= 2;
  }
  return ans;
}
std::vector<vl> dp2(1010, vl(1010));
vl dp(1010), tdp(1010), po(1010), po1(1010);
void __prec(int k) {
  lli temp = 0;
  for (int i = 0; i < 1010; i++) po[i] = mpow(8, i);
  for (int i = 0; i < 1010; i++) po1[i] = mpow(10, i);
  dp[0] = 1;
  for (int i = 1; i < 1010; i++) {
    for (int j = 0; j < max(1, i - k); j++) {
      temp = (2LL * po[i - j - 1] * dp[j]) % 1000000007;
      dp[i] = (dp[i] + temp) % 1000000007;
    }
  }
  for (int i = 1010 - 1; i >= 0; i--) {
    for (int j = 0; j < i; j++) {
      temp = (po[i - j] * dp[j]) % 1000000007;
      dp[i] = (dp[i] + temp) % 1000000007;
    }
  }
  for (int i = 0; i < 1010; i++)
    dp[i] = (mpow(10, i) - dp[i] + 1000000007) % 1000000007;
  for (int i = 1; i < 1010; i++)
    dp2[1][i] = (2ll * mpow(10, i - 1)) % 1000000007;
  for (int i = 2; i < 1010; i++) {
    dp2[i][i] = ((dp2[i - 1][i - 1] * 8LL) + dp2[1][i]) % 1000000007;
    for (int j = i + 1; j < 1010; j++)
      dp2[i][j] = (dp2[i][j - 1] * 10LL) % 1000000007;
  }
}
lli calc(string s, int k, bool low) {
  int n = ((lli)(s).size());
  int ind = -1, coun = 0, tind = -1, tcoun = 0;
  bool fl = 0, tfl = 0;
  lli ans = 0, temp;
  for (int i = 0; i < n; i++) {
    int cur = s[i] - '0';
    tind = ind;
    tcoun = coun;
    tfl = fl;
    for (int bit = 0; bit < cur; bit++) {
      if (bit == 4 || bit == 7) {
        tind = i;
        tcoun = coun + 1;
        if (ind >= 0 && tind - ind <= k) tfl = 1;
      }
      if (!tfl) {
        if (tind >= 0) {
          if (tind + k + 1 < n) {
            if (tind + k + 1 > i + 1) {
              temp = (po[tind + k - i] * dp[n - tind - k - 1]) % 1000000007;
              ans += temp;
              ans += dp2[tind + k - i][n - i - 1];
            } else
              ans += dp[n - i - 1];
          } else
            ans += dp2[n - i - 1][n - i - 1];
        } else
          ans += dp[n - i - 1];
      } else
        ans += po1[n - i - 1];
      ans %= 1000000007;
      tind = ind;
      tcoun = coun;
      tfl = fl;
    }
    if (cur == 4 || cur == 7) {
      if (ind >= 0 && i - ind <= k) fl = 1;
      ind = i;
      coun++;
    }
  }
  if (fl && low) ans = (ans + 1) % 1000000007;
  return ans;
}
int tejas_919(int kkkk) {
  lli n, m, k, q, u, v, temp = 0, ans = 0;
  cin >> q >> k;
  __prec(k);
  while (q--) {
    string s;
    ans = 0;
    cin >> s;
    ans -= calc(s, k, 0);
    cin >> s;
    ans += calc(s, k, 1);
    ans = ((ans % 1000000007) + 1000000007) % 1000000007;
    cout << ans << '\n';
  }
  return 0;
}
signed main() {
  if (!0) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
  }
  cout << fixed << setprecision(10);
  int t = 1;
  for (int i = 0; i < t; i++) {
    tejas_919(i + 1);
  }
  {};
  if (0) system("pause");
}
