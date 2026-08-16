#include <bits/stdc++.h>
using namespace std;
int main() {
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    int a[n];
    int b[n];
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    for (int i = 0; i < n; i++) {
      cin >> b[i];
    }
    unordered_map<int, int> mp;
    for (int i = n - 1; i >= 0; i--) {
      mp[a[i]] = i;
    }
    bool flag = true;
    for (int i = n - 1; i >= 0; i--) {
      if (a[i] == b[i]) {
        continue;
      }
      if (b[i] > a[i]) {
        if (mp.count(1) != 0 && mp[1] < i) {
          continue;
        }
      }
      if (b[i] < a[i]) {
        if (mp.count(-1) != 0 && mp[-1] < i) {
          continue;
        }
      }
      flag = false;
    }
    if (flag) {
      cout << "YES" << endl;
    } else
      cout << "NO" << endl;
  }
}
