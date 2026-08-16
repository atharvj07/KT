#include <bits/stdc++.h>
using namespace std;
long long int power(long long int a, long long int n) {
  if (n == 0) return 1;
  if ((n % 2) == 0)
    return (power((a * a), n / 2));
  else
    return (a * (power((a * a), n / 2)));
}
int main() {
  std::ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  ;
  long long int t;
  cin >> t;
  while (t--) {
    string a, b, c;
    cin >> a >> b >> c;
    long long int n = a.length();
    long long int k = 0;
    for (int i = 0; i < n; i++) {
      if (a[i] != c[i] && c[i] != b[i]) {
        k = 1;
        cout << "NO"
             << "\n";
        break;
      }
    }
    if (k == 0) {
      cout << "YES"
           << "\n";
    }
  }
  return 0;
}
