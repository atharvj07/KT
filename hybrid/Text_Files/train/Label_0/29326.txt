#include <bits/stdc++.h>
using namespace std;
int b[100001];
int main() {
  int n;
  cin >> n;
  int a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int ans = 0;
  for (int i = 2; i * i < 100000; i++) {
    int count = 0;
    for (int j = 0; j < n; j++) {
      if (a[j] % i == 0) {
        count++;
        while (a[j] % i == 0) {
          a[j] /= i;
        }
      }
    }
    ans = max(ans, count);
  }
  for (int i = 0; i < n; i++) {
    b[a[i]]++;
  }
  for (int i = 2; i < 1e5; i++) {
    ans = max(b[i], ans);
  }
  cout << max(1, ans) << endl;
  return 0;
}
