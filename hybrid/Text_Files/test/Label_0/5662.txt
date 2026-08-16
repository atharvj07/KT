#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m, k;
  cin >> n >> m >> k;
  vector<int> v(n);
  vector<int> c(m + 5, 0);
  for (int i = 0; i < n; i++) {
    cin >> v[i];
  }
  int l = 0, r = 0;
  int res = 1;
  c[v[0] - 1]++;
  int maxC = 1;
  int maxI = v[0] - 1;
  while (r < n) {
    if (c[v[r] - 1] > maxC) {
      maxC = c[v[r] - 1];
      maxI = v[r] - 1;
    }
    if (c[v[l] - 1] > maxC) {
      maxC = c[v[l] - 1];
      maxI = v[l] - 1;
    }
    if (r - l + 1 - maxC > k) {
      if (v[l] - 1 == maxI) {
        maxC--;
      }
      c[v[l] - 1]--;
      l++;
    } else if (r == n - 1) {
      break;
    } else {
      r++;
      c[v[r] - 1]++;
      if (c[v[r] - 1] > maxC) {
        maxC = c[v[r] - 1];
        maxI = v[r] - 1;
      }
      if (r - l + 1 - maxC <= k) {
        res = max(res, maxC);
      }
    }
  }
  cout << res;
  return 0;
}
