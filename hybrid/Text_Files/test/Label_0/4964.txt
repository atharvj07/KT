#include <bits/stdc++.h>
using namespace std;
const int N = 100005;
using ll = long long;
using ld = long double;
struct Point {
  ll x, y, z;
} a[2][N], p[2], x;
inline Point operator-(const Point &a, const Point &b) {
  return {a.x - b.x, a.y - b.y, a.z - b.z};
}
inline Point operator*(const Point &a, const Point &b) {
  return {a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x};
}
inline ll dot(const Point &a, const Point &b) {
  return a.x * b.x + a.y * b.y + a.z * b.z;
}
int n[2], o[N], s, t;
vector<pair<ld, pair<int, int>>> v;
inline int sgn(ll x) { return x > 0 ? 1 : x == 0 ? 0 : -1; }
int main() {
  ios::sync_with_stdio(false);
  int t1, t2, t3;
  for (int t = 0; t < 2; t++) {
    cin >> n[t];
    for (int i = 0; i < n[t]; i++)
      cin >> t1 >> t2 >> t3, a[t][i] = {t1, t2, t3};
    a[t][n[t]] = a[t][0];
    p[t] = (a[t][1] - a[t][0]) * (a[t][2] - a[t][0]);
  }
  x = p[0] * p[1];
  if (!dot(x, x)) {
    puts("NO");
    return 0;
  }
  for (int t = 0; t < 2; t++) {
    for (int i = 0; i <= n[t]; i++)
      o[i] = sgn(dot(a[t][i] - a[t ^ 1][0], p[t ^ 1]));
    for (int i = 0; i < n[t]; i++)
      if (o[i] != o[i + 1])
        v.push_back(
            {dot(a[t][i], x) + dot(a[t][i + 1] - a[t][i], x) *
                                   ld(dot(p[t ^ 1], a[t][i] - a[t ^ 1][0])) /
                                   dot(p[t ^ 1], a[t][i] - a[t][i + 1]),
             {t, o[i] - o[i + 1]}});
  }
  sort(v.begin(), v.end());
  ll sum = 0, tt = 0;
  for (auto &i : v)
    if (i.second.first)
      sum += tt * i.second.second;
    else
      tt += i.second.second;
  cout << (sum ? "YES" : "NO") << endl;
  return 0;
}
