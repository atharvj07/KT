#include <bits/stdc++.h>
using namespace std;
const int maxn = 4000006;
int a[maxn];
int main() {
  ios::sync_with_stdio(false);
  int n, r;
  long long int sum = 0;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> r;
    a[r]++;
  }
  int i = 0;
  while (i <= 2000001) {
    if (a[i] != 0) {
      a[i + 1] += a[i] / 2;
      sum += a[i] % 2;
    }
    i++;
  }
  cout << sum << endl;
  return 0;
}
