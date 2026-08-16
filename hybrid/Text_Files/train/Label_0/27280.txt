#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k;
  cin >> n >> k;
  vector<int> vec(n), res;
  for (auto &v : vec) {
    cin >> v;
  }
  if (k == 1) {
    return cout << vec[0], 0;
  }
  int l = 0;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
      l++;
      if (l == k) {
        return cout << vec[j - 1], 0;
      }
    }
  }
  return 0;
}
