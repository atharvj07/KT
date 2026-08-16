#include <bits/stdc++.h>
const int MAX = (const int)(1e5 + 11);
using namespace std;
static void solve(std::int32_t test) {
  int c1, c2, c3, c4;
  cin >> c1 >> c2 >> c3 >> c4;
  if (c1 == 0 && c4 == 0) {
    cout << (c3 == 0);
  } else {
    cout << (c1 == c4);
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  cout << setprecision(12) << fixed;
  solve(0);
  return 0;
}
