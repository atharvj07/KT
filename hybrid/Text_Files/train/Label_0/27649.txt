#include <bits/stdc++.h>
using namespace std;
long long id[1005];
long long root(long long x) {
  while (id[x] != x) {
    id[x] = id[id[x]];
    x = id[x];
  }
  return x;
}
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long n;
  cin >> n;
  for (long long i = 1; i <= n; i++) id[i] = i;
  vector<pair<long long, long long>> adj;
  vector<long long> a;
  for (long long i = 1; i < n; i++) {
    long long x, y;
    cin >> x >> y;
    if (root(x) != root(y)) {
      id[root(x)] = root(y);
    } else
      adj.push_back({x, y});
  }
  for (long long i = 1; i <= n; i++)
    if (id[i] == i) a.push_back(i);
  cout << a.size() - 1 << endl;
  for (long long i = 1; i < a.size(); i++) {
    cout << adj[i - 1].first << " " << adj[i - 1].second << " " << a[0] << " "
         << a[i] << "\n";
  }
}
