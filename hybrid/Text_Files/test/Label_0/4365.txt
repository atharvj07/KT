#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, m;
  cin >> n >> m;
  int mid = n * 2;
  for (int i = mid + 1, j = 1; i <= m || j <= m; i++, j++) {
    if (i <= m) cout << i << " ";
    if (j <= mid && j <= m) cout << j << " ";
  }
  return 0;
}
