#include <bits/stdc++.h>
using namespace std;
int n, k, sum, r, j, a[201];
char c;
string s;
int main() {
  cin >> n >> k >> s;
  for (int i = 0; i < n; i++) a[s[i]]++;
  a[200] = 400000;
  while (sum < k) {
    j++;
    sum += a[j];
  }
  r = k - sum + a[j];
  c = j;
  for (int i = 0; i < n; i++) {
    if (s[i] == j) {
      if (r == 0)
        cout << s[i];
      else
        r--;
    } else if (s[i] > j) {
      cout << s[i];
    }
  }
  return 0;
}
