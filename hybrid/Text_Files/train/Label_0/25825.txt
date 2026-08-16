#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  int n, m;
  cin >> n >> m;
  vector<long long> h(n);
  for (int i = 0; i < n; ++i) {
    cin >> h[i];
  }
  vector<long long> p(m);
  for (int i = 0; i < m; ++i) {
    cin >> p[i];
  }
  long long left = 0, right = 100000000000000000ll;
  while (left < right) {
    long long center = (left + right) / 2;
    int done = 0;
    for (int i = 0; i < n; ++i) {
      const long long first = p[done];
      for (; done < m; ++done) {
        const long long last = p[done];
        const long long cost =
            min(abs(h[i] - first), abs(h[i] - last)) + (last - first);
        if (cost > center) {
          break;
        }
      }
    }
    if (done >= m) {
      right = center;
    } else {
      left = center + 1;
    }
  }
  cout << left << endl;
  return 0;
}
