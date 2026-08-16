#include <bits/stdc++.h>
using namespace std;
const long long oo = 1e15;
int N;
string str;
pair<int, int> a, b;
long long dist(int x1, int y1, int x2, int y2) {
  return pow(x1 - x2, 2) + pow(y1 - y2, 2);
}
long double EPS = 1e-6;
bool cmp(const pair<int, int>& p1, const pair<int, int>& p2) {
  return dist(p1.first, p1.second, a.first, a.second) <
         dist(p2.first, p2.second, a.first, a.second);
}
void solve() {
  cin >> N;
  cin >> a.first >> a.second;
  cin >> b.first >> b.second;
  vector<pair<int, int>> v(N);
  for (pair<int, int>& el : v) cin >> el.first >> el.second;
  sort((v.begin()), (v.end()), cmp);
  long long ans = oo;
  for (int i = 0; i < N; ++i) {
    long long r1 = dist(v[i].first, v[i].second, a.first, a.second);
    long long r2 = 0;
    for (int j = i + 1; j < N; ++j) {
      r2 = max(r2, dist(v[j].first, v[j].second, b.first, b.second));
    }
    ans = min(ans, r1 + r2);
  }
  long long r2 = 0;
  for (int j = 0; j < N; ++j)
    r2 = max(r2, dist(v[j].first, v[j].second, b.first, b.second));
  cout << min(ans, r2);
}
int main() {
  ios_base ::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
  ;
  int tt;
  tt = 1;
  while (tt--) {
    solve();
  }
  return 0;
}
