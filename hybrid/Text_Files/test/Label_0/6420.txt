#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int a;
  map<int, int> b;
  int res = 0;
  for (int i = 0; i < n; i++) {
    cin >> a;
    b[a]++;
    res = max(res, b[a]);
  }
  cout << res;
  return 0;
}
