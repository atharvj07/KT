#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int n, i, j, c = 0;
    cin >> n;
    char a[n];
    cin >> a;
    for (i = 0; i < n - 1; i++) {
      if (a[i] == a[i + 1]) c++;
    }
    cout << (c / 2) + (c % 2) << " ";
    cout << "\n";
  }
  return 0;
}
