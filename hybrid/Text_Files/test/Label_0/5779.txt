#include <bits/stdc++.h>
using namespace std;
long long gcd(long long a, long long b) {
  while (b) {
    swap(a, b);
    b %= a;
  }
  return a;
}
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int _ = 1;
  while (_--) {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int cnt1, cnt0;
    cnt1 = cnt0 = 0;
    int cnt = 0;
    for (int i = 0; i < n; i++) {
      if (n % (i + 1) == 0 && i + 1 != n && i + 1 != 1) {
        cnt++;
      }
      if (s[i] - '0') {
        cnt1++;
      } else {
        cnt0++;
      }
    }
    if (cnt1 == 0) {
      cout << n << endl;
      continue;
    }
    if (n == 1) {
      cout << (s[0] == '1' ? 0 : 1) << endl;
      continue;
    }
    cnt = n - 1;
    vector<bool> cur(n, true);
    cur[1] = cnt1 % 2 == 0;
    if (!cur[1]) {
      cnt--;
    }
    for (int i = 2; i < n; i++) {
      long long g = gcd(i, n);
      if (g == i) {
        vector<int> b(i);
        for (int j = 0; j < n; j++) {
          b[j % i] += s[j] - '0';
        }
        bool ok = true;
        for (int i : b) {
          if (i % 2) {
            ok = false;
            break;
          }
        }
        cur[i] = ok;
      } else {
        cur[i] = cur[g];
      }
      if (!cur[i]) {
        cnt--;
      }
    }
    cout << cnt << endl;
  }
}
