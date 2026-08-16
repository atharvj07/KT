#include <bits/stdc++.h>
using namespace std;
const int maxN = 1e5 + 1;
const int mod = 1e9 + 7;
long long n, a[maxN];
inline void FastInput() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
}
void ReadInput() {
  cin >> n;
  for (int i = 1; i <= n; i++) cin >> a[i];
}
void Solve() {
  long long res = 0;
  for (int i = 2; i <= n; i++) {
    if (a[i] == 0 && a[i + 1] == 1 && a[i - 1] == 1) {
      res++;
      a[i + 1] = 0;
    }
  }
  cout << res;
}
int main() {
  FastInput();
  ReadInput();
  Solve();
}
