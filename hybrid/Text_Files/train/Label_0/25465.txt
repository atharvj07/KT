#include <bits/stdc++.h>
using namespace std;
char a[27];
int n, m, i, k;
string s, t1, t2;
int main() {
  iostream::sync_with_stdio(0);
  cin.tie();
  cin >> n >> m;
  cin >> s;
  for (i = 1; i <= 26; i++) a[i] = i + 96;
  for (i = 1; i <= m; i++) {
    cin >> t1 >> t2;
    for (k = 1; k <= 26; k++) {
      if (a[k] == t1[0])
        a[k] = t2[0];
      else if (a[k] == t2[0])
        a[k] = t1[0];
    }
  }
  for (i = 0; i < n; i++) cout << a[s[i] - 96];
}
