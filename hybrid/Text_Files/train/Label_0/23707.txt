#include <bits/stdc++.h>
using namespace std;
const int INF_int = 100000000;
const long long INF_ll = 1000000000000000;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  string a;
  cin >> a;
  int n = a.size();
  int m;
  cin >> m;
  int b[n];
  for (int i = 0; i < n; i++) {
    b[i] = 0;
    if (i != n - 1 && a[i] == a[i + 1]) {
      b[i] = 1;
    }
  }
  int sum[n];
  sum[0] = b[0];
  for (int i = 1; i < n; i++) {
    sum[i] = b[i] + sum[i - 1];
  }
  for (int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;
    x--;
    y--;
    if (x != 0)
      cout << sum[y - 1] - sum[x - 1] << "\n";
    else
      cout << sum[y - 1] << "\n";
  }
}
