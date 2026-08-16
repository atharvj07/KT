#include <bits/stdc++.h>
using namespace std;
const int MAX = 2e5, mod = 1e9 + 7;
int main() {
  string x;
  cin >> x;
  int n = x.size();
  long long sum = 0, prev = 0;
  int c = 0;
  bool tb = 0;
  for (int i = n - 1; i >= 0; i--) {
    if (x[i] == 'a')
      sum = (sum + prev + 1) % mod, c++;
    else if (x[i] == 'b')
      prev = (prev + (c * (prev + 1)) % mod) % mod, c = 0;
  }
  cout << sum;
}
