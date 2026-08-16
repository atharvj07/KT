#include <bits/stdc++.h>
using namespace std;
int main() {
  int n, A, B, C, T;
  cin >> n >> A >> B >> C >> T;
  long long int sum = 0;
  for (int i = 0; i < n; i++) {
    int t;
    cin >> t;
    if (C >= B)
      sum += 0LL + (C - B) * (T - t) + A;
    else
      sum += A + 0LL;
  }
  cout << sum << endl;
  return 0;
}
