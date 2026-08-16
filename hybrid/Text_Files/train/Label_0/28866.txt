#include <bits/stdc++.h>
using namespace std;
int r[105];
int main() {
  int n, m;
  cin >> n >> m;
  int right = 0;
  for (int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;
    if (a <= right && b > right) right = b;
  }
  if (right == m)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;
  return 0;
}
