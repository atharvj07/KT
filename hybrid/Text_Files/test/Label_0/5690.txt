#include <bits/stdc++.h>
using namespace std;
void showpq(priority_queue<long long> pq) {
  while (!pq.empty()) {
    cout << pq.top() << " ";
    pq.pop();
  }
  cout << "\n";
}
signed main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  map<string, pair<priority_queue<long long>, priority_queue<long long>>> mp;
  map<string, priority_queue<long long>> pal;
  long long k, n, val, a, b;
  cin >> k >> n;
  string s, p;
  while (k--) {
    cin >> s >> val;
    p = s;
    reverse(p.begin(), p.end());
    if (p == s)
      pal[s].push(val);
    else if (mp.count(p))
      mp[p].second.push(val);
    else
      mp[s].first.push(val);
  }
  long long fans = 0;
  for (auto &y : mp) {
    while (!(y.second.first.empty()) && !(y.second.second.empty()) &&
           (y.second.first.top() + y.second.second.top()) > 0) {
      fans += (y.second.first.top() + y.second.second.top());
      y.second.first.pop();
      y.second.second.pop();
    }
  }
  for (auto &y : pal) {
    while (y.second.size() >= 2) {
      a = y.second.top();
      y.second.pop();
      b = y.second.top();
      y.second.pop();
      if (a + b < 0) {
        y.second.push(a);
        break;
      }
      if (b < 0) y.second.push(-b);
      fans += a + b;
    }
  }
  a = 0;
  for (auto y : pal) {
    if (!y.second.empty()) a = max(y.second.top(), a);
  }
  fans += a;
  cout << fans << "\n";
  return 0;
}
