#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  int cnt0 = 0, pos;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    if (!a[i]) {
      ++cnt0;
      pos = i;
    }
  }
  int x;
  for (int i = 0; i < k; ++i) {
    cin >> x;
  }
  if (cnt0 == 1) {
    a[pos] = x;
  }
  int res = 0;
  for (int i = 1; i < n; ++i) {
    if (a[i] > a[i - 1]) {
      ++res;
    }
  }
  if (res == n - 1) {
    cout << "No";
  } else if (cnt0 > 1) {
    cout << "Yes";
  } else {
    cout << "Yes";
  }
  return 0;
}
