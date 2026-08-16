#include <bits/stdc++.h>
using namespace std;
long long n, t;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cin >> t;
  for (long long i = 1; i <= t; i++) {
    cin >> n;
    cout << (n - 1) / 2 << endl;
  }
}
