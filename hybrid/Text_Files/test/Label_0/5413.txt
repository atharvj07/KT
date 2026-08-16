#include <bits/stdc++.h>
using namespace std;
int main() {
  long long n;
  cin >> n;
  long long total = 0;
  for (long long i = 0; i < n; i++) {
    long long x;
    cin >> x;
    total += x;
  }
  int count = 0;
  for (long long i = 1; i <= 5; i++) {
    count += ((total + i) % (n + 1) == 1 ? 0 : 1);
  }
  cout << count;
}
