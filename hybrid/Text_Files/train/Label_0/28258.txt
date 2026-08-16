#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  int a[n];
  for (int i = 0; i < n; i++) cin >> a[i];
  int spike, cnt = 0;
  for (int i = 1; i < n; i++)
    if (a[i] < a[i - 1]) {
      cnt++;
      spike = i;
    }
  if (cnt == 0)
    cout << 0 << endl;
  else if (cnt > 1 || a[n - 1] > a[0])
    cout << -1 << endl;
  else
    cout << n - spike << endl;
  return 0;
}
