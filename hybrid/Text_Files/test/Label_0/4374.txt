#include <bits/stdc++.h>
using namespace std;
int main() {
  long long t;
  cin >> t;
  while (t--) {
    long long n, x;
    cin >> n >> x;
    long long a[n];
    for (long long i = 0; i < n; i++) {
      cin >> a[i];
    }
    long long count = 0;
    sort(a, a + n);
    long long no = 1;
    long long sum = 0;
    for (long long i = n - 1; i >= 0; i--) {
      sum += a[i];
      if ((sum / (no * 1.0)) >= x) {
        count++;
        no++;
      } else {
        break;
      }
    }
    cout << count << "\n";
  }
  return 0;
}
