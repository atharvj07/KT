#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, minn = 1000000000, minn1 = 1000000000;
  cin >> n;
  vector<int> a(n);
  for (int i = (0); i < (n); i++) cin >> a[i];
  for (int i = (1); i < (n - 1); i++) {
    minn = 0;
    for (int j = (1); j < (n); j++) {
      if (!(i == j || i + 1 == j)) minn = max(minn, a[j] - a[j - 1]);
    }
    minn = max(minn, a[i + 1] - a[i - 1]);
    minn1 = min(minn, minn1);
  }
  cout << minn1 << endl;
  return 0;
}
