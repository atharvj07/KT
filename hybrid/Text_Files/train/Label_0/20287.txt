#include <bits/stdc++.h>
using namespace std;
int inversions(const vector<int> &p) {
  int cnt = 0;
  int n = p.size();
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
      if (p[i] > p[j]) {
        ++cnt;
      }
    }
  }
  return cnt;
}
double solve(vector<int> p, int k) {
  if (k == 0) {
    return inversions(p);
  }
  int n = p.size();
  double ans = 0.0;
  for (int i = 0; i < n; ++i) {
    double prob = 2.0 / (n * (n + 1));
    for (int j = i; j < n; ++j) {
      vector<int> np = p;
      reverse(np.begin() + min(i, j), np.begin() + max(i, j) + 1);
      ans += prob * solve(np, k - 1);
    }
  }
  return ans;
}
int main() {
  int n, k;
  cin >> n >> k;
  vector<int> p(n);
  for (int &x : p) {
    cin >> x;
  }
  cout << setprecision(10) << fixed << solve(p, k) << endl;
  return 0;
}
