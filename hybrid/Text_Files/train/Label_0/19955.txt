#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int t;
  cin >> t;
  while (t--) {
    int n, m;
    cin >> n >> m;
    vector<int> p;
    pair<int, int> a[m];
    int x, s = 0;
    for (int i = 1; i <= n; i++) cin >> x, p.push_back(x);
    if (n == 2)
      cout << -1 << endl;
    else if (m < n)
      cout << -1 << endl;
    else {
      sort(p.begin(), p.end());
      for (int i = 1; i <= n; i++) {
        if (i <= n - 1) {
          a[i - 1].first = i;
          a[i - 1].second = i + 1;
          s += p[i - 1] + p[i];
        }
      }
      a[m - 1].first = n, a[m - 1].second = 1;
      s += p[n - 1] + p[0];
      cout << s << endl;
      for (int i = 1; i <= m; i++)
        cout << a[i - 1].first << " " << a[i - 1].second << endl;
    }
  }
}
