#include <bits/stdc++.h>
using namespace std;
int n, m, c, x;
int a[100005];
long long mars[2 * 100005];
int main() {
  scanf("%d %d %d", &n, &m, &c);
  for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
  for (int i = 1; i <= m; ++i) {
    scanf("%d", &x);
    mars[i] += x;
    mars[i + (n - m + 1)] -= x;
  }
  long long act = 0;
  for (int i = 1; i <= n; ++i) {
    act += mars[i];
    mars[i] = act + a[i];
    mars[i] %= c;
  }
  for (int i = 1; i <= n; ++i) {
    cout << mars[i] << ' ';
  }
  cout << '\n';
  return 0;
}
