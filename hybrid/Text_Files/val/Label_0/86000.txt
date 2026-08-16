#include <bits/stdc++.h>
using namespace std;
int main() {
  long long int n, m, a, b;
  cin >> n >> m >> a >> b;
  cout << min((m - n % m) * a, n % m * b);
}
