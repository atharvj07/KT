#include <bits/stdc++.h>
using namespace std;
struct hash_pair {
  template <class T1, class T2>
  size_t operator()(const pair<T1, T2>& p) const {
    auto hash1 = hash<T1>{}(p.first);
    auto hash2 = hash<T2>{}(p.second);
    return hash1 ^ hash2;
  }
};
long long t;
long long m = 1e9 + 7;
long long arr[200005], cnt[200005];
multiset<long long> st[200005], s;
vector<long long> v[200005];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ;
  long long a, b, c, d, e, f, g, i, j;
  cin >> a >> b;
  for (i = 0; i < a; i++) {
    cin >> arr[i];
  }
  sort(arr, arr + a);
  for (i = 1; i <= b; i++) {
    cin >> cnt[i];
  }
  g = 0;
  long long chk = 0;
  s.insert(200005);
  for (i = a - 1; i >= 0; i--) {
    d = arr[i];
    f = cnt[d];
    f--;
    auto it = s.lower_bound(f);
    auto n = s.begin();
    if (f < *n) {
      g++;
      s.insert(1);
      st[1].insert(g);
      v[g].push_back(arr[i]);
    } else {
      if (f < *it) it--;
      e = *it;
      s.erase(it);
      s.insert(e + 1);
      auto tt = st[e].begin();
      j = *tt;
      st[e].erase(tt);
      st[e + 1].insert(j);
      v[j].push_back(arr[i]);
    }
  }
  cout << g << endl;
  for (i = 1; i <= g; i++) {
    cout << v[i].size();
    for (j = 0; j < v[i].size(); j++) {
      cout << ' ' << v[i][j];
    }
    cout << endl;
  }
  return 0;
}
