#include <bits/stdc++.h>
using namespace std;
ostream &operator<<(ostream &output,
                    const pair<long long int, long long int> &p) {
  output << p.first << " " << p.second;
  return output;
}
istream &operator>>(istream &input, pair<long long int, long long int> &p) {
  input >> p.first >> p.second;
  return input;
}
template <typename T>
void inline println(vector<T> args) {
  for (T i : args) cout << i << " ";
  cout << '\n';
}
void amax(long long int &a, long long int b) { a = max(a, b); }
void amin(long long int &a, long long int b) { a = min(a, b); }
long long int INF = 1e18;
long long int MOD = 998244353;
vector<set<long long int>> adj;
void solve() {
  long long int n, h, d;
  cin >> n >> d >> h;
  if (h < d - (d / 2)) {
    cout << -1 << '\n';
    return;
  }
  if (n > 2 && d == 1) {
    cout << -1 << '\n';
    return;
  }
  if (n == 2) {
    cout << "1 2" << '\n';
    return;
  }
  set<long long int> nodes;
  for (long long int i = 0; i < n; i++) nodes.insert(i + 1);
  nodes.erase(1);
  long long int prev = 1;
  for (long long int i = 0; i < h; i++) {
    long long int curr = *nodes.begin();
    nodes.erase(nodes.begin());
    cout << prev << " " << curr << '\n';
    prev = curr;
  }
  prev = 1;
  for (long long int i = 0; i < d - h; i++) {
    long long int curr = *nodes.begin();
    nodes.erase(nodes.begin());
    cout << prev << " " << curr << '\n';
    prev = curr;
  }
  if (d - h > 0)
    prev = 1;
  else
    prev = 2;
  for (long long int i = 0; i < n - d - 1; i++) {
    long long int curr = *nodes.begin();
    nodes.erase(nodes.begin());
    cout << prev << " " << curr << '\n';
  }
}
signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long int t = 1;
  for (long long int i = 0; i < t; i++) {
    solve();
  }
  return 0;
}
