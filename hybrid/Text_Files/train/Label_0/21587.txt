#include <bits/stdc++.h>
using namespace std;
const int inf = 1e9;
const int MOD = 1e9 + 7;
const int N = 100100;
int a, b;
int main() {
  cin >> a >> b;
  if (a == b) {
    cout << "infinity";
    return 0;
  }
  if (a < b) {
    cout << 0;
    return 0;
  }
  int x = a - b;
  int k = 0;
  for (int i = 1; i * i <= x; i++)
    if (x % i == 0) {
      if (a % i == b) k++;
      if (i != x / i && a % (x / i) == b) k++;
    }
  cout << k;
  return 0;
}
