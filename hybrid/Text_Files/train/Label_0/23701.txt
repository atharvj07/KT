#include <bits/stdc++.h>
using namespace std;
long long int i, j, k, a, b, n;
int main() {
  long long int n, cc[101] = {0}, m = 0, s = 0;
  for (i = 0; i < 5; i++) {
    cin >> n;
    s += n;
    cc[n]++;
    if (cc[n] == 3 || cc[n] == 2) m = max(m, cc[n] * n);
  }
  cout << s - m << endl;
}
