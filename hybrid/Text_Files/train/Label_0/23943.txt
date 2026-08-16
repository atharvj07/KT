#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    vector<int> vc(n);
    for (int i = 0; i < n; i++) {
      cin >> vc[i];
    }
    int i;
    int count = 0;
    for (i = 0; i < n - 2; i++) {
      if (vc[i] + vc[i + 1] <= vc[n - 1]) {
        cout << i + 1 << " " << i + 2 << " " << n << endl;
        count++;
        break;
      }
    }
    if (count == 0) cout << -1 << endl;
  }
}
