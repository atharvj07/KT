#include <bits/stdc++.h>
using namespace std;
const int N = 1000008;
void calc(unsigned long long int &a, unsigned long long int &b) {
  if (a == 0 || b == 0) return;
  if (a >= 2 * b) {
    a = a % 2 * b;
    calc(a, b);
  } else if (b >= 2 * a) {
    b = b % 2 * a;
    calc(a, b);
  }
}
int main() {
  ios_base::sync_with_stdio(false);
  unsigned long long int n, m;
  cin >> n >> m;
  while (n > 0 && m > 0) {
    if (n >= 2 * m) {
      n = n % (2 * m);
      continue;
    } else if (m >= 2 * n) {
      m = m % (2 * n);
      continue;
    } else {
      break;
    }
  }
  cout << n << " " << m << "\n";
  return 0;
}
