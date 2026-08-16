#include <bits/stdc++.h>
using namespace std;
long long n, k;
string s;
long long cache[101][105];
long long dp(long long pos, long long tk) {
  if (tk > k) return -1e18;
  if (pos == n) return tk == k;
  long long ans = tk == k;
  if (cache[pos][tk] != -1) return cache[pos][tk];
  if (s[pos] != '?')
    return cache[pos][tk] = ans + dp(pos + 1, (s[pos] == 'N') ? tk + 1 : 0);
  return cache[pos][tk] = ans + max(dp(pos + 1, tk + 1), dp(pos + 1, 0));
}
int32_t main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  ;
  cin >> n >> k >> s;
  memset(cache, -1, sizeof(cache));
  cout << ((dp(0, 0) > 0) ? "YES" : "NO");
}
