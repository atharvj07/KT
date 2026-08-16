#include <bits/stdc++.h>
using namespace std;
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ;
  int t;
  cin >> t;
  while (t--) {
    long long n;
    cin >> n;
    long long cnt = 0, hh = 0;
    int nn = sqrt(n);
    int dd = n / nn;
    if (n % nn) dd++;
    cout << dd + nn - 2 << endl;
  }
  return 0;
}
