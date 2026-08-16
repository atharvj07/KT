#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 10;
pair<int, int> operator-(pair<int, int> a, pair<int, int> b) {
  return pair<int, int>(a.first - b.first, a.second - b.second);
}
long long operator%(pair<int, int> a, pair<int, int> b) {
  return 1LL * a.first * b.second - 1LL * a.second * b.first;
}
long long operator*(pair<int, int> a, pair<int, int> b) {
  return 1LL * a.first * b.first + 1LL * a.second * b.second;
}
long long dist(pair<int, int> a, pair<int, int> b) { return (a - b) * (a - b); }
int CCW(pair<int, int> a, pair<int, int> b, pair<int, int> c) {
  pair<int, int> p1 = b - a, p2 = c - a;
  if (p1 % p2 > 0) return 1;
  if (p1 % p2 < 0) return -1;
  return 0;
}
pair<int, int> cpiv;
bool comp(pair<int, int> a, pair<int, int> b) {
  int type = CCW(cpiv, a, b);
  if (type == 0) return dist(cpiv, a) < dist(cpiv, b);
  return CCW(cpiv, a, b) == 1;
}
struct polygon {
  vector<pair<int, int> > v;
  vector<pair<int, int> > ans;
  void add_point(const pair<int, int>& a) { v.push_back(a); }
  void clear() { v.clear(); }
  void normalize() {
    ans.clear();
    for (auto& i : v)
      if (i < v.back()) swap(i, v.back());
    ans.push_back(v.back());
    v.pop_back();
    cpiv = ans[0];
    sort(v.begin(), v.end(), comp);
    for (auto i : v) {
      bool keep = 1;
      while (ans.size() > 1) {
        int n = ans.size();
        int type = CCW(ans[n - 2], ans[n - 1], i);
        if (type == 1) break;
        if (type == -1) {
          ans.pop_back();
          continue;
        }
        keep = 0;
        if (dist(ans[n - 2], i) > dist(ans[n - 2], ans[n - 1])) ans[n - 1] = i;
        break;
      }
      if (keep) ans.push_back(i);
    }
    if (ans.size() > 2) {
      int n = ans.size();
      if (CCW(ans[0], ans[n - 1], ans[n - 2]) == 0) ans.pop_back();
    }
  }
  vector<long long> gethash() {
    int n = ans.size();
    vector<long long> samp;
    for (int i = 1; i < n - 1; i++) {
      samp.push_back(dist(ans[i], ans[i - 1]));
      samp.push_back((ans[i - 1] - ans[i]) * (ans[i + 1] - ans[i]));
    }
    samp.push_back(dist(ans[n - 1], ans[n - 2]));
    return samp;
  }
} pol[2];
pair<int, int> a[2][N];
string solve(vector<long long>& a, vector<long long>& b) {
  vector<int> tr(a.size(), 0);
  for (int i = 1; i < a.size(); i++) {
    tr[i] = tr[i - 1];
    while (tr[i] != 0 && a[tr[i]] != a[i]) tr[i] = tr[tr[i] - 1];
    if (a[i] == a[tr[i]]) tr[i]++;
  }
  int len = 0;
  for (int i = 0; i < b.size(); i++) {
    long long val = b[i];
    while (len != 0 && a[len] != val) len = tr[len - 1];
    if (a[len] == val) len++;
    if (len == a.size()) return "YES";
  }
  return "NO";
}
int main() {
  int n1, n2;
  cin >> n1 >> n2;
  for (int i = 0; i < n1; i++) cin >> a[0][i].first >> a[0][i].second;
  for (int i = 0; i < n2; i++) cin >> a[1][i].first >> a[1][i].second;
  pol[0].clear();
  pol[1].clear();
  for (int i = 0; i < n1; i++) pol[0].add_point(a[0][i]);
  for (int i = 0; i < n2; i++) pol[1].add_point(a[1][i]);
  pol[0].normalize();
  pol[1].normalize();
  if (pol[0].ans.size() != pol[1].ans.size()) {
    cout << "NO";
    return 0;
  }
  int nt = pol[0].ans.size();
  for (int i = 0; i < nt; i++) pol[0].ans.push_back(pol[0].ans[i]);
  vector<long long> a = pol[0].gethash();
  vector<long long> b = pol[1].gethash();
  cout << solve(b, a);
}
