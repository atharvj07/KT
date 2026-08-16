#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const int base = 1e9;
const int MAX = 2e5;
const long double EPS = 1e-10;
const long double PI = acos(-1.);
int n;
int main() {
  ios_base::sync_with_stdio(0);
  cin >> n;
  if (n % 2) {
    cout << 7;
    n -= 3;
  }
  while (n) {
    cout << 1;
    n -= 2;
  }
  return 0;
}
