#include <bits/stdc++.h>
using namespace std;
int32_t main() {
  long long t;
  cin >> t;
  while (t--) {
    long long n, m, a, b;
    cin >> n >> m >> a >> b;
    if ((n * a) != (m * b))
      cout << "NO" << endl;
    else {
      cout << "YES" << endl;
      long long A[n][m];
      memset(A, 0, sizeof(A));
      long long x = 0;
      for (long long i = 0; i < n; i++) {
        long long c = a;
        while (c--) {
          A[i][x] = 1;
          x++;
          x = x % m;
        }
      }
      for (long long i = 0; i < n; i++) {
        for (long long j = 0; j < m; j++) cout << A[i][j];
        cout << endl;
      }
    }
  }
}
