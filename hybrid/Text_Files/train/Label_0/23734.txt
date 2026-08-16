#include <bits/stdc++.h>
using namespace std;
bool cmp(std::pair<int64_t, int64_t> a, std::pair<int64_t, int64_t> b) {
  return (a.first - a.second) > (b.first - b.second);
}
int main() {
  int n, a, b;
  cin >> n >> a >> b;
  vector<std::pair<int64_t, int64_t> > c(n);
  for (int i = 0; i < n; ++i) {
    cin >> c[i].first >> c[i].second;
  }
  int64_t result = 0;
  for (int i = 0; i < n; ++i) {
    result += c[i].second;
  }
  sort(c.begin(), c.end(), cmp);
  for (int i = 0; i < min(n, b - 1); ++i) {
    if (c[i].first < c[i].second) {
      break;
    }
    result -= c[i].second;
    result += c[i].first;
  }
  int64_t sum = result;
  if (b == 0) {
    cout << sum << endl;
    return 0;
  }
  for (int i = 0; i < n; ++i) {
    int64_t res = sum;
    if (c[i].first > c[i].second && i < b - 1) {
      res -= c[i].first;
      res += (c[i].first * (1 << a));
      if (b - 1 < n && c[b - 1].first > c[b - 1].second) {
        res -= c[b - 1].second;
        res += c[b - 1].first;
      }
    } else {
      res -= c[i].second;
      res += (c[i].first * (1 << a));
    }
    result = max(res, result);
  }
  cout << result << endl;
  return 0;
}
