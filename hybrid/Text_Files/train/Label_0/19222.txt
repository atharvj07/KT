#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, k;
  cin >> n >> k;
  int a[k];
  vector<int> b;
  for (int i = 1; i <= k; i++) {
    cin >> a[i];
  }
  for (int i = 1; i <= n * k; i++) {
    int count = 0;
    for (int j = 1; j <= k; j++) {
      if (a[j] == i) count = 1;
    }
    if (count == 0) b.push_back(i);
  }
  int j = 0;
  for (int i = 1; i <= k; i++) {
    int p = n - 1;
    cout << a[i] << " ";
    while (p > 0) {
      p--;
      cout << b[j] << " ";
      j++;
    }
    cout << "\n";
  }
  return 0;
}
