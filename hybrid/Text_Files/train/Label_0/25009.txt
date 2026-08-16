#include <bits/stdc++.h>
using namespace std;
int main() {
  int i, j, n, arr[200004], m = INT_MAX;
  char a[200004];
  cin >> n;
  cin >> a;
  for (i = 0; i < n; i++) cin >> arr[i];
  int flag = 0;
  if (n == 1)
    cout << "-1\n";
  else {
    i = 0;
    while (i < n) {
      while (a[i] == 'L' && i < n) i++;
      while (a[i] == 'R' && i < n) i++;
      if (i == n) {
        break;
      } else {
        flag = 1;
        j = arr[i] - arr[i - 1];
        j = j / 2;
        m = min(j, m);
      }
    }
    if (flag == 1)
      cout << m;
    else
      cout << "-1";
  }
}
