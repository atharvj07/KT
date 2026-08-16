#include <bits/stdc++.h>

using namespace std;

int main(void) {
  int n;
  while (cin >> n, n) {
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }

    int ans = 0;
    for (int i = 0; i < n - 1; i++) {
      for (int j = i + 1; j < n; j++) {
        if (a[j] < a[i]) {
          ans++;
        }
      }
    }

    cout << ans << endl;
  }

  return 0;
}
