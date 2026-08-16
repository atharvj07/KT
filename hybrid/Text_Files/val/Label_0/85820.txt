#include <bits/stdc++.h>
using namespace std;
int N, R, vals[1 << 18];
double sum = 0;
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout << fixed << setprecision(18);
  cin >> N >> R;
  for (int i = 0; i < (1 << N); i++) {
    cin >> vals[i];
    sum += vals[i];
  }
  cout << sum / (1 << N) << '\n';
  for (int i = 0; i < R; i++) {
    int x, y;
    cin >> x >> y;
    sum += y - vals[x];
    vals[x] = y;
    cout << sum / (1 << N) << '\n';
  }
  return 0;
}
