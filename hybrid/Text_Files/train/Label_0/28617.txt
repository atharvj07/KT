#include <bits/stdc++.h>
using namespace std;
constexpr int N = 100000 + 3;
char s[N];
long long a[N][27];
long long ch[27 + 'a'];
long long m1, m2, ans, m3;
int main() {
  cin >> (s);
  int len = strlen(s);
  for (int i = 0; i < len; i++) {
    ch[s[i]]++;
    for (int j = 0; j < 26; j++) {
      a[i][j] = ch[j + 'a'];
    }
    m1 = max(m1, ch[s[i]]);
  }
  m2 = m1 * (m1 - 1) / 2;
  ans = max(m1, m2);
  for (int i = 0; i < 26; i++) {
    for (int j = 0; j < 26; j++) {
      if (i == j) continue;
      m3 = 0;
      for (int l = 0; l < len; l++) {
        if (s[l] == i + 'a') m3 += ch[j + 'a'] - a[l][j];
      }
      ans = max(ans, m3);
    }
  }
  cout << ans << endl;
  return 0;
}
