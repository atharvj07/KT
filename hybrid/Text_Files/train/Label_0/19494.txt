#include <bits/stdc++.h>
using namespace std;
pair<int, int> p1, p2;
set<pair<int, int>> s;
set<pair<pair<int, int>, pair<int, int>>> s1;
vector<pair<int, int>> pos;
int dis(pair<int, int> p1, pair<int, int> p2) {
  return abs(p1.first - p2.first) + abs(p1.second - p2.second);
};
bool check(pair<int, int> a, pair<int, int> b, pair<int, int> c,
           pair<int, int> d) {
  int x = dis(a, b), y = dis(c, d), z = dis(a, d), q = dis(b, c);
  if (!x or !y or !z or !q) return 0;
  return x == y && z == q;
}
void solve(int testcase) {
  for (int i = (0); i <= (3); i++) {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    p1 = {x1, y1};
    p2 = {x2, y2};
    if (x1 != x2 && y1 != y2) {
      cout << "NO";
      return;
    }
    if (p1 == p2) {
      cout << "NO";
      return;
    }
    if (s1.find({p1, p2}) != s1.end()) {
      cout << "NO";
      return;
    }
    s1.insert({p1, p2});
    s1.insert({p2, p1});
    s.insert(p1);
    s.insert(p2);
  }
  if (((int)s.size()) == 4) {
    for (auto p : s) pos.push_back(p);
    vector<int> idx = {0, 1, 2, 3};
    do {
      auto a = pos[idx[0]];
      auto b = pos[idx[1]];
      auto c = pos[idx[2]];
      auto d = pos[idx[3]];
      if (check(a, b, c, d)) {
        cout << "YES";
        return;
      }
    } while (next_permutation(idx.begin(), idx.end()));
    cout << "NO";
  } else
    cout << "NO";
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  cout << setprecision(10);
  clock_t b = clock();
  int t = 1;
  for (int tt = (1); tt <= (t); tt++) solve(tt);
  clock_t e = clock();
  cerr << (double(e - b) / CLOCKS_PER_SEC) << " sec";
  return 0;
}
