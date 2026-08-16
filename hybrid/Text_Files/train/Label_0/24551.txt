#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, x, y, k = 0;
  cin >> n >> x >> y;
  string a;
  cin >> a;
  if (n == 0) {
    cout << 0;
    return 0;
  }
  string b = "";
  for (int i = a.size() - x; i < a.size(); i++) {
    b += a[i];
  }
  reverse(b.begin(), b.end());
  for (int i = 0; i < b.size(); i++) {
    if (b[i] == '1' && i != y) k++;
    if (b[i] == '0' && i == y) k++;
  }
  cout << k;
  return 0;
}
