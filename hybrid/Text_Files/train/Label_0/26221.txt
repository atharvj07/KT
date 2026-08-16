#include <bits/stdc++.h>
const long long inf = 1e18 + 7, N = 500007;
using namespace std;
long long ar[N], fr[N];
long long n, m, a, b, i, j, k, l, sum, cnt, ans, mx, mn = inf;
string s[55];
vector<long long> v;
int32_t main() {
  cin >> n;
  for (i = 1; i <= n; i++) cin >> ar[i], fr[ar[i]]++;
  i = 4;
  if (n == 1)
    cout << ar[1] << endl;
  else if (n == 2) {
    if (fr[1] == 1)
      cout << 2 << ' ' << 1 << endl;
    else
      cout << ar[1] << ' ' << ar[2] << endl;
  } else if (n == 3) {
    if (fr[1] == 1)
      cout << 2 << ' ' << 1 << ' ' << 2 << endl;
    else if (fr[1] == 2)
      cout << 2 << ' ' << 1 << ' ' << 1 << endl;
    else
      cout << ar[1] << ' ' << ar[2] << ' ' << ar[3] << endl;
  } else if (fr[1] > 2)
    cout << 1 << ' ' << 1 << ' ' << 1, fr[1] -= 3;
  else {
    cout << 2;
    fr[2]--;
    if (fr[1])
      cout << ' ' << 1, i = 3, fr[1]--;
    else
      i = 2;
  }
  for (; i <= n; i++) {
    if (fr[2])
      cout << ' ' << 2, fr[2]--;
    else if (fr[1] > 1)
      cout << ' ' << 1 << ' ' << 1, fr[1] -= 2, i++;
    else
      cout << ' ' << 1;
  }
}
