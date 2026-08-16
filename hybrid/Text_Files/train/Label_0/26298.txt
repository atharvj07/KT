#include <bits/stdc++.h>
using namespace std;
int a[22 + 1], sortat[22 + 1];
int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
    sortat[i] = a[i];
  }
  sort(sortat, sortat + n);
  for (int i = 0; i < n; ++i) {
    int k = 0;
    while (sortat[k] < a[i]) ++k;
    k = (k + 1) % n;
    cout << sortat[k] << " ";
  }
  cout << "\n";
  return 0;
}
