#include <bits/stdc++.h>
using namespace std;
bool next_perm(vector<int>& v, int n, int k) {
  for (int i = k - 1; i >= 0;) {
    if (v[i] == n - k + i) {
      i--;
    } else {
      v[i] += 1;
      i++;
      while (i < k) {
        v[i] = v[i - 1] + 1;
        i++;
      }
      return true;
    }
  }
  return false;
}
vector<int> get_all(vector<int>& v, int k, int n, bool with_zero) {
  if (!k) {
    return vector<int>(1, 0);
  }
  vector<int> res, perm(k);
  for (int i = 0; i < k; i++) {
    perm[i] = i;
  }
  do {
    if (with_zero && perm[0] != 0) {
      continue;
    }
    if (!with_zero && perm[0] == 0) {
      continue;
    }
    int tmp = 0;
    for (auto& x : perm) {
      tmp += v[x];
    }
    res.emplace_back(tmp);
  } while (next_perm(perm, n, k));
  sort(res.begin(), res.end());
  return res;
}
void find(vector<int>& v, int k, int n, int s, vector<int>& res_a,
          vector<int>& res_b, bool with_zero) {
  if (!k) {
    for (int i = 0; i < n; i++) {
      res_b.emplace_back(v[i]);
    }
    return;
  }
  vector<int> perm(k);
  for (int i = 0; i < k; i++) {
    perm[i] = i;
  }
  do {
    if (with_zero && perm[0] != 0) {
      continue;
    }
    if (!with_zero && perm[0] == 0) {
      continue;
    }
    int tmp = 0;
    for (auto& x : perm) {
      tmp += v[x];
    }
    if (tmp == s) {
      for (int i = 0; i < n; i++) {
        if (find(perm.begin(), perm.end(), i) != perm.end()) {
          res_a.emplace_back(v[i]);
        } else {
          res_b.emplace_back(v[i]);
        }
      }
      return;
    }
  } while (next_perm(perm, n, k));
}
void get_best(int n, vector<int>& a, vector<int>& b, vector<int>& res, int k,
              int s) {
  vector<int> all_a = get_all(a, k, n, true);
  vector<int> all_b = get_all(b, n - k, n, false);
  int diff = res[2];
  for (auto x : all_a) {
    auto it = lower_bound(all_b.begin(), all_b.end(), s / 2 - x - b[0]);
    if (it == all_b.end()) {
      continue;
    }
    if (diff > abs(s / 2 - (x + *it) - b[0])) {
      diff = abs(s / 2 - (x + *it) - b[0]);
      res[0] = x;
      res[1] = *it;
      res[2] = diff;
      res[3] = k;
    }
  }
}
pair<vector<int>, vector<int>> solve(int n, vector<int>& a, vector<int>& b) {
  int s_a = 0, s_b = 0;
  for (int i = 0; i < n; i++) {
    s_a += a[i];
    s_b += b[i];
  }
  vector<int> res = {s_a, 0, 1000000000, n};
  for (int k = 0; k <= n; k++) {
    get_best(n, a, b, res, k, s_a + s_b + a[0] + b[0]);
  }
  vector<int> res_a, res_b;
  find(a, res[3], n, res[0], res_a, res_b, true);
  find(b, n - res[3], n, res[1], res_a, res_b, false);
  sort(res_a.begin(), res_a.end());
  sort(res_b.begin(), res_b.end());
  reverse(res_b.begin(), res_b.end());
  return make_pair(res_a, res_b);
}
int main() {
  int n;
  cin >> n;
  vector<int> a(n), b(n), tmp(2 * n);
  for (int i = 0; i < n; i++) {
    cin >> tmp[i];
  }
  for (int i = 0; i < n; i++) {
    cin >> tmp[i + n];
  }
  sort(tmp.begin(), tmp.end());
  a[0] = tmp[0];
  b[0] = tmp[1];
  for (int i = 1; i < n; i++) {
    a[i] = tmp[1 + i];
    b[i] = tmp[n + i];
  }
  auto p = solve(n, a, b);
  int res1 = 0, res2 = 0;
  for (auto x : p.first) {
    cout << x << " ";
    res1 += x;
  }
  cout << "\n";
  for (auto x : p.second) {
    cout << x << " ";
    res2 += x;
  }
  cout << "\n";
  res1 += p.second.back();
  res2 += p.first.front();
  return 0;
}
