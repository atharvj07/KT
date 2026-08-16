#include <bits/stdc++.h>
using namespace std;
int a[10001] = {0};
int b[10001] = {0};
int s = 0;
int sn = 0;
int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> a[i];
  for (int i = 1; i <= n; i++) {
    cin >> b[i];
    if (b[i] > a[i])
      s++;
    else if (b[i] < a[i])
      sn++;
  }
  if (sn == 0)
    cout << "-1" << endl;
  else
    cout << s / sn + 1 << endl;
  return 0;
}
