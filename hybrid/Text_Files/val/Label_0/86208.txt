#include <bits/stdc++.h>
using namespace std;
const int MM = 1200000;
bool solve(long long int p, long long int q, vector<long long int> x) {
  if (p <= 0 || q <= 0) {
    return 0;
  }
  if (x.size() == 1) {
    return (p / q == x.back() && p == x.back() * q);
  }
  long long int tp = x.back();
  x.pop_back();
  if (abs(p / q - tp) > 2) {
    return 0;
  }
  return solve(q, p - q * tp, x);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  long long int P, Q;
  cin >> P >> Q;
  int N;
  cin >> N;
  vector<long long int> A(N);
  for (int i = 0; i < N; i++) {
    cin >> A[N - i - 1];
  }
  if (solve(P, Q, A)) {
    cout << "YES";
  } else {
    cout << "NO";
  }
  return 0;
}
