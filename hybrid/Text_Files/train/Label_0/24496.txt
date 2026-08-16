#include <bits/stdc++.h>
using namespace std;
void solve() {
  long long i, n, x1, y1, x2, y2, temp, champ, sum, count,
      ans = 0, maxx = -1, minn = 100000000000, modd = 1000000007, N, flag = 0,
      q;
  string str, ptr;
  cin >> str;
  sum = 0;
  n = str.size();
  for (i = 0; i < n; i++) {
    if (str[i] == 'A') {
      ans++;
    } else if (ans > 0) {
      ans--;
      str[i] = '1';
      sum++;
    }
  }
  for (i = 0; i < n; i++) {
    if (str[i] == 'A') {
      if (sum) {
        str[i] = '1';
        sum--;
      } else {
        break;
      }
    }
  }
  for (i = 0; i < n; i++) {
    if (str[i] != '1') {
      ptr += str[i];
    }
  }
  i = 0;
  ans = 0;
  count = 0;
  n = ptr.size();
  while (i < n - 1) {
    if (ptr[i] == 'B' && ptr[i + 1] == 'B') {
      i += 2;
      ans += 2;
    } else {
      i++;
    }
  }
  count = n - ans;
  cout << count;
  cout << endl;
}
int main() {
  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
