#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  long double a, b, c;
  cin >> a >> b >> c;
  vector<int_fast64_t> am;
  int_fast64_t k = 1, max = pow(10, 9);
  int_fast64_t f = pow(k, a) * b + c;
  while (k <= 81 && f <= max) {
    int_fast64_t sum = 0, n = f;
    while (f != 0) {
      sum += f % 10;
      f /= 10;
    }
    if (sum == k) am.emplace_back(n);
    k++;
    f = pow(k, a) * b + c;
  }
  cout << am.size() << "\n";
  for (int_fast64_t i = 0; i < am.size(); i++) {
    cout << am[i] << " ";
  }
}
