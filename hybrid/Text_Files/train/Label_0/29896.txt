#include <bits/stdc++.h>
using namespace std;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, swaps;
  cin >> n >> swaps;
  long long res = 0;
  for (int l = 0, r = n - 1; l < r and l < swaps;) {
    res += (r - l++);
    res += (r-- - l);
  }
  cout << res;
}
