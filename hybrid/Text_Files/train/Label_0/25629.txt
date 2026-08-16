#include <bits/stdc++.h>
using namespace std;
int main() {
  srand(1373737);
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int n, k;
  cin >> n >> k;
  string s;
  cin >> s;
  int p = 0, len = 0;
  while (p < s.size()) {
    if (s[p] != 'N') {
      p++;
      continue;
    }
    int now = 0;
    while (p < s.size() && s[p] == 'N') {
      now++;
      p++;
    }
    len = max(len, now);
  }
  if (len > k) {
    cout << "NO";
    return 0;
  }
  if (k == 0) {
    cout << "YES";
    return 0;
  }
  vector<bool> fix(n);
  for (int i = 0; i < n; i++) {
    if (s[i] == '?')
      s[i] = 'N';
    else
      fix[i] = true;
  }
  p = 0;
  len = 0;
  while (p < s.size()) {
    if (s[p] != 'N') {
      p++;
      continue;
    }
    int now = 0, start = p;
    while (p < s.size() && s[p] == 'N') {
      now++;
      if (now == k) {
        if ((start - 1 < 0 ||
             (!fix[start - 1] && s[start - 1] == 'N' || s[start - 1] == 'Y')) &&
            (p + 1 >= n ||
             (!fix[p + 1] && s[p + 1] == 'N' || s[p + 1] == 'Y'))) {
          cout << "YES";
          return 0;
        } else {
          now--;
          start++;
        }
      }
      p++;
    }
  }
  cout << "NO";
  return 0;
}
