#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  while (cin >> n >> m) {
    string st1[1005], st2[1005];
    for (int i = 1; i <= n; i++) cin >> st1[i];
    for (int i = 1; i <= m; i++) cin >> st2[i];
    int ans = 0;
    for (int i = 1; i <= n; i++)
      for (int j = 1; j <= m; j++)
        if (st1[i] == st2[j]) ans++;
    n -= ans / 2;
    m -= ans / 2;
    if (ans % 2) m--;
    if (n > m)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}
