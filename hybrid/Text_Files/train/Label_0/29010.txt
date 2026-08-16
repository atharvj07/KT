#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, x;
  cin >> n >> x;
  if (x == 2) {
    cout << 0;
    return 0;
  }
  int a[100000];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (a[i] == 1) {
      cout << 1;
      return 0;
    }
  }
  sort(a, a + n);
  int next_prime = 2;
  int prime[100002];
  int ans = 0;
  int i = 0;
  while (next_prime < x) {
    while (i < n && a[i] < next_prime) i++;
    if (i == n || a[i] != next_prime) {
      cout << -1;
      return 0;
    }
    bool found = false;
    prime[ans++] = next_prime;
    while (!found && next_prime < x) {
      found = true;
      next_prime++;
      for (int j = 0; j < ans; j++) {
        if (prime[j] * prime[j] > next_prime) break;
        if (next_prime % prime[j] == 0) {
          found = false;
          break;
        }
      }
    }
  }
  cout << ans;
  return 0;
}
