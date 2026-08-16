#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, l[2005], r[2005], t, k;
  cin >> t;
  while (t) {
    int q = 0, next = 0;
    cin >> n;
    for (int i = 0; i < n; i++) {
      cin >> l[i] >> r[i];
      if (i == 0) {
        next = l[i] + 1;
        cout << l[i] << " ";
        continue;
      }
      if (r[i] < next) {
        cout << 0 << " ";
      } else if (l[i] <= next) {
        cout << next << " ";
        next++;
      } else {
        cout << l[i] << " ";
        next = l[i] + 1;
      }
    }
    cout << endl;
    t--;
  }
  return 0;
}
