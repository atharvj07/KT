#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n, k;
  cin >> n >> k;
  long long c[27] = {0};
  string s;
  cin >> s;
  for (int i = 0; i < n; i++) {
    c[s[i] - 'A'] += 1;
  }
  long long cc = 0L;
  long long num = 0L;
  while (true) {
    long long maxi = 0L;
    int idx = -1;
    for (int i = 0; i < 26; i++) {
      long long cache = maxi;
      maxi = max(maxi, c[i]);
      if (cache != maxi) idx = i;
    }
    c[idx] = 0;
    cc += maxi;
    if (cc >= k) {
      cout << num + (maxi - (cc - k)) * (maxi - (cc - k));
      return 0;
    } else {
      num += maxi * maxi;
    }
  }
  return 0;
}
