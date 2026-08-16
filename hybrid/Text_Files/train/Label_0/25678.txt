#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, x, a, b;
  vector<int> v;
  vector<int> v2;
  cin >> n >> x;
  for (int i = 0; i < n; i++) {
    cin >> a >> b;
    if (a < b) {
      v.push_back(a);
      v2.push_back(b);
    } else {
      v.push_back(b);
      v2.push_back(a);
    }
  }
  sort(v.begin(), v.end());
  sort(v2.begin(), v2.end());
  vector<int>::iterator it;
  vector<int>::iterator ip;
  it = unique(v.begin(), v.end());
  v.resize(distance(v.begin(), it));
  ip = unique(v.begin(), v.end());
  v2.resize(distance(v.begin(), ip));
  if (v[n - 1] > v2[0])
    cout << -1;
  else if (v.size() == 1) {
    if (x < v[n - 1])
      cout << abs(v[n - 1] - x);
    else if (x > v2[0])
      cout << abs(v2[0] - x);
    else
      cout << 0;
  } else if (x >= v[n - 1] && x <= v2[0]) {
    cout << 0;
  } else {
    int c = abs(v[n - 1] - x);
    int d = abs(v2[0] - x);
    if (c < d)
      cout << c;
    else
      cout << d;
    return 0;
  }
}
