#include <bits/stdc++.h>
using namespace std;
int a[100001];
int main() {
  ios::sync_with_stdio(false);
  ;
  cin.tie(0);
  ;
  int i, j, n, pos;
  cin >> n;
  for (i = 1; i <= n; i++) cin >> a[i];
  if (n == 1) {
    if (a[1] == 0) {
      cout << "YES"
           << "\n";
      cout << "0";
      return 0;
    } else {
      cout << "NO";
      return 0;
    }
  }
  if (a[n] == 1) {
    cout << "NO";
    return 0;
  }
  if (a[n - 1] == 1) {
    cout << "YES"
         << "\n";
    for (i = 1; i < n; i++) cout << a[i] << "->";
    cout << a[n];
    return 0;
  }
  pos = -1;
  for (i = n - 2; i >= 1; i--) {
    if (a[i] == 0) {
      pos = i;
      break;
    }
  }
  if (pos == -1) {
    cout << "NO";
    return 0;
  }
  cout << "YES"
       << "\n";
  for (i = 1; i < pos; i++) cout << a[i] << "->";
  cout << "(0->(";
  for (i = pos + 1; i <= n - 2; i++) cout << a[i] << "->";
  cout << "0))->0";
  return 0;
}
