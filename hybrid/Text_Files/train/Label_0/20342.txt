#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, l, a[100009], s = 0;
  cin >> n >> l;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    s += a[i];
  }
  s += n - 1;
  if (s == l)
    cout << "YES" << endl;
  else
    cout << "NO" << endl;
  return 0;
}
