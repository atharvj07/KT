#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  long long int a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int p[n];
  int q[n];
  p[0] = abs(a[n - 1] - a[0]);
  q[0] = abs(a[1] - a[0]);
  p[n - 1] = p[0];
  q[n - 1] = abs(a[n - 1] - a[n - 2]);
  cout << q[0] << " " << p[0] << endl;
  for (int i = 1; i < n - 1; i++) {
    p[i] = max(abs(a[i] - a[0]), abs(a[i] - a[n - 1]));
    q[i] = min(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1]));
    cout << q[i] << " " << p[i] << endl;
  }
  cout << q[n - 1] << " " << p[n - 1] << endl;
  return 0;
}
