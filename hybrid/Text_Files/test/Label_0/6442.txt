#include <bits/stdc++.h>
using namespace std;
const long long mod = 1e9 + 7;
bool sortinrev(const pair<int, int> &a, const pair<int, int> &b) {
  return (a.first > b.first);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(NULL);
  cout.tie(NULL);
  long long int n, m;
  cin >> n >> m;
  long long int a[n][m], arr[n][m];
  long long int ans[n];
  for (long long int i = 0; i < n; ++i) {
    for (long long int j = 0; j < m; ++j) {
      cin >> a[i][j];
      arr[i][j] = a[i][j];
    }
    ans[i] = 1;
  }
  long long int x = a[0][0];
  for (int i = 1; i < n; ++i) {
    x = x ^ a[i][0];
  }
  if (x != 0) {
    cout << "TAK" << '\n';
    for (long long int i = 0; i < n; ++i) {
      cout << "1 ";
    }
  } else {
    bool temp = false;
    for (long long int i = 0; i < n; ++i) {
      sort(a[i], a[i] + m);
      if (a[i][0] != a[i][m - 1]) {
        temp = true;
        for (long long int j = 0; j < m; ++j) {
          if (arr[i][j] != arr[i][0]) {
            ans[i] = j + 1;
            break;
          }
        }
        break;
      }
    }
    if (temp) {
      cout << "TAK" << '\n';
      for (long long int i = 0; i < n; ++i) {
        cout << ans[i] << " ";
      }
    } else {
      cout << "NIE";
      return 0;
    }
  }
  return 0;
}
