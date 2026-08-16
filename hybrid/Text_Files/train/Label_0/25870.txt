#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  int maxi = 0, ans = 0;

  for (int i = 0; i < N; i++) {
    int H;
    cin >> H;
    if (H >= maxi) maxi = H, ans++;
  }

  cout << ans << "\n";
}