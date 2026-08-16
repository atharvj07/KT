#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, k = 1;
  cin >> n;
  if (n == 1) {
    cout << "1\n1";
  } else if (n == 2) {
    cout << "1\n1 1";
  } else {
    vector<bool> isprime(n + 2, true);
    vector<long long int> A(n + 2, 1);
    for (int i = 2; i <= n + 1; i++) {
      if (isprime[i]) {
        for (int j = 2 * i; j <= n + 1; j = j + i) {
          isprime[j] = false;
        }
      }
    }
    cout << 2 << "\n";
    for (int i = 2; i <= n + 1; i++) {
      if (isprime[i])
        cout << 1 << " ";
      else
        cout << 2 << " ";
    }
  }
  return 0;
}
