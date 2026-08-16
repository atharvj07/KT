#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(0);
  long long n;
  cin >> n;
  long long bestA = 1, bestB = n;
  for (int i = 2; i * i <= n; ++i) {
    if (n % i == 0) {
      bestA = i;
      bestB = n / i;
    }
  }
  cout << bestA << " " << bestB;
}
