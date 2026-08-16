#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;
using vi = vector<int>;
using vl = vector<long>;
using vll = vector<ll>;
using vb = vector<bool>;
using vvb = vector<vb>;
using vvi = vector<vector<int> >;
using ii = pair<int, int>;
using vii = vector<ii>;
using vs = vector<string>;
using msi = map<string, int>;
using iss = istringstream;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  string s;
  cin >> s;
  int n = s.length();
  for (int i = int(0); i <= int(n - 1); i++) s[i] -= 'a';
  vb seen(26, false);
  for (int i = int(0); i <= int(n - 1); i++) seen[s[i]] = true;
  int ds = accumulate(seen.begin(), seen.end(), 0);
  vll ans(ds + 1, 0);
  for (int k = int(1); k <= int(ds); k++) {
    vector<deque<int> > dq(26, deque<int>());
    int l = 0, r = -1;
    int uniq = 0;
    int upos = 0;
    ll cnt = 0;
    while (l < n) {
      while (true) {
        if (r == n - 1) break;
        if (uniq == k && !dq[s[r + 1]].size() > 0) break;
        r++;
        if (dq[s[r]].size() == 0) {
          uniq++;
          upos = r;
        }
        dq[s[r]].push_back(r);
        if (uniq == k) cnt++;
      }
      ans[k] += cnt;
      dq[s[l]].pop_front();
      if (dq[s[l]].size() == 0) {
        uniq--;
        cnt = 0;
      } else {
        int nupos = max(upos, dq[s[l]][0]);
        cnt = max(0ll, cnt - (nupos - upos));
        upos = nupos;
      }
      l++;
    }
  }
  cout << ds << '\n';
  for (int k = int(1); k <= int(ds); k++) cout << ans[k] << '\n';
  return 0;
}
