#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, t, res = 0;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> t;
    res += (t * i) - (i - 1);
  }
  cout << res << endl;
}
