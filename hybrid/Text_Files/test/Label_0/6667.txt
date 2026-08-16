#include <bits/stdc++.h>
using namespace std;
const long long mod = 1000000007;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  long long a, b, c;
  cin >> a >> b >> c;
  if (a > (b + c))
    cout << '+';
  else if ((a + c) < b)
    cout << '-';
  else {
    if (a == b && c == 0)
      cout << 0;
    else
      cout << '?';
  }
  cout << endl;
}
