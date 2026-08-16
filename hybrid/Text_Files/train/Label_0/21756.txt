#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  vector<vector<int>> a(n, vector<int>(m));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) cin >> a[i][j];
  }
  vector<vector<int>> b(n, vector<int>(m));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) cin >> b[i][j];
  }
  vector<vector<int>> bb;
  for (int i = 0; i < n; ++i) bb.push_back(b[i]);
  sort(bb.begin(), bb.end());
  bb.erase(unique(bb.begin(), bb.end()), bb.end());
  vector<vector<int>> who_a(bb.size());
  vector<vector<int>> who_b(bb.size());
  for (int i = 0; i < n; ++i) {
    int ind = lower_bound(bb.begin(), bb.end(), a[i]) - bb.begin();
    if (ind == (int)bb.size() || bb[ind] != a[i]) {
      cout << -1 << endl;
      return 0;
    }
    who_a[ind].push_back(i);
    ind = lower_bound(bb.begin(), bb.end(), b[i]) - bb.begin();
    who_b[ind].push_back(i);
  }
  vector<int> p(n);
  for (int i = 0; i < (int)bb.size(); ++i) {
    if (who_a[i].size() != who_b[i].size()) {
      cout << -1 << endl;
      return 0;
    }
    for (int j = 0; j < (int)who_a[i].size(); ++j) {
      p[who_a[i][j]] = who_b[i][j];
    }
  }
  vector<int> q(n);
  for (int i = 0; i < n; ++i) q[p[i]] = i;
  vector<bool> good(n, 0);
  vector<int> cnt_bad(m, 0), cnt_kek(m, 0);
  for (int j = 0; j < m; ++j) {
    for (int i = 0; i < n - 1; ++i) {
      if (a[q[i]][j] < a[q[i + 1]][j]) ++cnt_kek[j];
      if (a[q[i]][j] > a[q[i + 1]][j]) ++cnt_bad[j];
    }
  }
  vector<int> ans;
  while (true) {
    bool ok = true;
    for (int i = 0; i < n - 1; ++i) ok &= good[i] || q[i] < q[i + 1];
    if (ok) break;
    int col = -1;
    for (int j = 0; j < m; ++j) {
      if (cnt_bad[j] == 0 && cnt_kek[j] > 0) {
        col = j;
        break;
      }
    }
    if (col == -1) break;
    ans.push_back(col);
    for (int i = 0; i < n - 1; ++i) {
      if (!good[i] && a[q[i]][col] < a[q[i + 1]][col]) {
        good[i] = true;
        for (int j = 0; j < m; ++j) {
            if (a[q[i]][j] < a[q[i + 1]][j]) --cnt_kek[j];
            if (a[q[i]][j] > a[q[i + 1]][j]) --cnt_bad[j];
        }
      }
    }
  }
  bool ok = true;
  for (int i = 0; i < n - 1; ++i) ok &= good[i] || q[i] < q[i + 1];
  if (ok) {
    cout << (int)ans.size() << endl;
    reverse(ans.begin(), ans.end());
    for (int i : ans) cout << i + 1 << " ";
    cout << endl;
  } else {
    cout << -1 << endl;
  }
  return 0;
}
