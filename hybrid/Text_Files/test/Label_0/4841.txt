#include <bits/stdc++.h>
using namespace std;
const int N = 100000;
int a[N];
void solve() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  sort(a, a + n);
  int j = 0;
  while (j < n - 1) {
    if (a[j] != a[j + 1]) {
      if (a[j] * 2 > a[j + 1]) {
        cout << "YES";
        return;
      }
    }
    j++;
  }
  cout << "NO";
}
int main() {
  solve();
  getchar();
  getchar();
}
