#include <bits/stdc++.h>
using namespace std;
const long double pi = 3.141592653589793238462643383279502884;
const long long xd[] = {-1, 0, 1, 0};
const long long yd[] = {0, -1, 0, 1};
long long XX[] = {-1, -1, -1, 0, 0, 1, 1, 1};
long long YY[] = {-1, 0, 1, -1, 1, -1, 0, 1};
long long expo(long long a, long long b, long long m);
long long mmi(long long a, long long m);
void ipgraph(long long m);
const long long N = 5 * (1e5) + 10;
vector<vector<long long> > adj(N);
long long a[N];
void solve() {}
struct Compare {
  bool operator()(pair<long long, long long> &p1,
                  pair<long long, long long> &p2) {
    long long diff1 = p1.second - p1.first;
    long long diff2 = p2.second - p2.first;
    return diff1 < diff2;
  }
};
int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long n, q;
  cin >> n >> q;
  set<long long> s;
  for (long long i = 0; i < n; i++) {
    cin >> a[i];
    s.insert(a[i]);
  }
  sort(a, a + n);
  map<pair<long long, long long>, long long> m;
  priority_queue<pair<long long, long long>,
                 vector<pair<long long, long long> >, Compare>
      pq;
  for (long long i = 0; i < n - 1; i++) {
    pq.push({a[i], a[i + 1]});
    m[{a[i], a[i + 1]}] = 1;
  }
  long long ans;
  if (n != 1)
    ans = a[n - 1] - a[0] - (pq.top().second - pq.top().first);
  else
    ans = 0;
  cout << ans << "\n";
  long long minz = a[0], maxz = a[n - 1];
  while (q--) {
    long long x, y;
    cin >> y >> x;
    if (y) {
      minz = min(minz, x);
      maxz = max(maxz, x);
      if (s.empty()) {
        s.insert(x);
        cout << 0 << "\n";
        continue;
      }
      auto itl = s.lower_bound(x);
      auto itr = s.upper_bound(x);
      if (itr == s.end()) {
        maxz = x;
        itr--;
        pq.push({*itr, x});
        m[{*itr, x}] = 1;
        s.insert(x);
      } else if (itl == s.begin()) {
        minz = x;
        pq.push({x, *itl});
        m[{x, *itl}] = 1;
        s.insert(x);
      } else {
        itl--;
        m[{*itl, *itr}] = 0;
        s.insert(x);
        pq.push({*itl, x});
        pq.push({x, *itr});
        m[{x, *itr}] = 1;
        m[{*itl, x}] = 1;
      }
    } else {
      s.erase(x);
      if (s.empty()) {
        cout << 0 << "\n";
        minz = INT_MAX;
        maxz = INT_MIN;
        continue;
      }
      if (minz == x) {
        m[{x, *s.begin()}] = 0;
        minz = *s.begin();
      } else if (maxz == x) {
        m[{*s.rbegin(), x}] = 0;
        maxz = *s.rbegin();
      } else {
        auto itl = s.lower_bound(x);
        auto itr = s.upper_bound(x);
        itl--;
        m[{x, *itr}] = 0;
        m[{*itl, x}] = 0;
        m[{*itl, *itr}] = 1;
        pq.push({*itl, *itr});
      }
    }
    while (!pq.empty() && m[{pq.top().first, pq.top().second}] == 0) pq.pop();
    if (pq.empty()) {
      cout << 0 << "\n";
      continue;
    }
    ans = maxz - minz - (pq.top().second - pq.top().first);
    cout << ans << "\n";
  }
  return 0;
}
void ipgraph(long long m) {
  long long i, u, v;
  while (m--) {
    cin >> u >> v;
    u--, v--;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }
}
long long expo(long long a, long long b, long long m) {
  if (b == 0) return 1;
  if (b == 1) return a;
  long long val = (expo(a, b / 2, m) * expo(a, b / 2, m)) % m;
  if (b & 1)
    return (val * a) % m;
  else
    return val;
}
long long mmi(long long a, long long m) { return expo(a, m - 2, m); }
