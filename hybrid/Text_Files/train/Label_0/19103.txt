#include <bits/stdc++.h>
using namespace std;
long long n, m, i, mx, a[100001], k, L, R, q, w, l, r, b[10000], s, e, j;
vector<long long> verr;
vector<pair<long long, char>> ans;
int main() {
  cin >> n;
  for (i = 1; i <= n; i++) cin >> a[i];
  cin >> k;
  l = 1;
  for (i = 1; i <= k; i++) cin >> b[i];
  for (i = 1; i <= k; i++) {
    l = i;
    while (a[i] < b[i] && l <= n) {
      if (a[l] != a[l + 1] && l + 1 <= n) {
        if (l + 2 <= n && a[l] + a[l + 1] < b[i]) {
          if (a[l] + a[l + 1] != a[l + 2]) {
            if (a[l] > a[l + 1])
              ans.push_back(make_pair(l, 'R'));
            else
              ans.push_back(make_pair(l + 1, 'L'));
            a[l] += a[l + 1];
            for (j = l + 1; j < n; j++) a[j] = a[j + 1];
            n--;
            l = i;
          } else
            l++;
        } else {
          if (a[l] > a[l + 1])
            ans.push_back(make_pair(l, 'R'));
          else
            ans.push_back(make_pair(l + 1, 'L'));
          a[l] += a[l + 1];
          for (j = l + 1; j < n; j++) a[j] = a[j + 1];
          n--;
          l = i;
        }
      } else
        l++;
    }
    if (a[i] != b[i]) {
      cout << "NO";
      return 0;
    }
  }
  if (n != k) {
    cout << "NO";
    return 0;
  }
  cout << "YES" << '\n';
  for (i = 0; i < ans.size(); i++)
    cout << ans[i].first << " " << ans[i].second << '\n';
}
