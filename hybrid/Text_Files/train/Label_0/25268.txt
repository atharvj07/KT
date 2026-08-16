#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, t;
  cin >> n >> t;
  long double base = 1.000000011;
  cout.precision(20);
  cout << n * pow(base, t) << endl;
  return 0;
}
