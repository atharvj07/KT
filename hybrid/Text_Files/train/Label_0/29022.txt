#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  long long int n, m, s;
  cin >> n >> m >> s;
  long long int a1 = 0;
  long long int a2 = 0;
  for (long long int i = 0; i < m; i++) {
    if ((i / s) + ((m - 1 - i) / s) == (m - 1) / s) {
      a1++;
    }
  }
  for (long long int i = 0; i < n; i++) {
    if ((i / s) + ((n - 1 - i) / s) == (n - 1) / s) {
      a2++;
    }
  }
  std::cout << a1 * a2 << std::endl;
  return 0;
}
