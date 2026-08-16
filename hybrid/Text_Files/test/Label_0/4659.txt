#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int t;
  cin >> t;
  while (t--) {
    long long int n, a, b, c, d;
    cin >> n >> a >> b >> c >> d;
    if (((c + d) / n) < (a - b))
      cout << "No" << endl;
    else if (((a + b) * n) < (c - d))
      cout << "No" << endl;
    else
      cout << "Yes" << endl;
  }
  return 0;
}
