#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, x, i;
  cin >> n;
  int a[n + 1], b[n + 1], m[n + 1], f[n + 1];
  for (i = 1; i <= n; i++) {
    cin >> a[i];
  }
  for (i = 1; i <= n; i++) {
    cin >> b[i];
    f[b[i]] = i;
  }
  for (i = 1; i <= n; i++) {
    m[i] = f[a[i]];
  }
  int ma = m[1];
  int c = 0;
  for (i = 2; i <= n; i++) {
    if (m[i] < ma) c++;
    ma = max(m[i], ma);
  }
  cout << c << "\n";
}
