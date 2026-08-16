#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 5;
long long int n, cnt1;
vector<long long int> v(N);
map<long long int, long long int> m;
bool f(long long int x) {
  m.clear();
  for (long long int i = (long long int)0; i <= (long long int)n - 1; i++)
    m[v[i]]++;
  vector<long long int> last(x, 1);
  long long int in = 2, cnt = x;
  m[1] -= x;
  while (m[in] > 0 && cnt > 0) {
    long long int inc = m[in];
    long long int cc = min(cnt, inc);
    m[in] -= cc;
    cnt = cc;
    for (long long int i = (long long int)0; i <= (long long int)cc - 1; i++)
      last[i] = in;
    in *= 2;
  }
  multiset<long long int> la;
  for (long long int i = (long long int)0; i <= (long long int)x - 1; i++)
    la.insert(last[i]);
  for (auto x : m) {
    long long int in = x.first, cnt = x.second;
    for (long long int i = (long long int)1; i <= (long long int)cnt; i++) {
      auto it = la.lower_bound((in + 1) / 2);
      if (it == la.end()) return false;
      la.erase(it);
    }
  }
  return true;
}
int main() {
  cin >> n;
  for (long long int i = (long long int)0; i <= (long long int)n - 1; i++)
    cin >> v[i], cnt1 += (v[i] == 1);
  long long int l = 0, r = cnt1 + 1;
  while (l < r - 1) {
    long long int m = l + (r - l) / 2;
    if (f(m))
      r = m;
    else
      l = m;
  }
  long long int mi = r;
  if (mi > cnt1) {
    cout << -1 << "\n";
    return 0;
  }
  for (long long int i = (long long int)mi; i <= (long long int)cnt1; i++)
    cout << i << " ";
}
