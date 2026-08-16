#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, c1, c2, p = 0, r;
  cin >> n >> c1 >> c2;
  char g;
  for (long long int i = 0; i < n; i++) {
    cin >> g;
    if (g == '1') p++;
  }
  long long int minr = -1;
  for (int i = 1; i <= p; i++) {
    r = i * c1 + c2 * ((n % i) * (n / i) * (n / i) +
                       (i - (n % i)) * (n / i - 1) * (n / i - 1));
    if (r < minr || minr == -1) minr = r;
  }
  cout << minr;
}
