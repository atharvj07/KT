#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  vector<long long> tmp;
  int n, k;
  cin >> n >> k;
  long long mas[n], ans = 0;
  for (int i = 0; i < (int)(n); ++i) cin >> mas[i];
  vector<pair<long long, long long> > ext;
  string s;
  cin >> s;
  for (int i = 0; i < (int)(s.length()); ++i) {
    ext.push_back(make_pair(mas[i], s[i]));
  }
  for (long long i = 0; i < s.length(); i++) {
    long long start = i, loop = k;
    while (s[i] == s[i + 1] && i < s.length() - 1) i++;
    for (long long j = start; j <= i; j++) {
      tmp.push_back(ext[j].first);
    }
    sort(tmp.begin(), tmp.end());
    for (long long i = tmp.size() - 1; i >= 0; i--) {
      ans += tmp[i];
      loop--;
      if (loop <= 0) break;
    }
    tmp.clear();
  }
  cout << ans;
  return 0;
}
