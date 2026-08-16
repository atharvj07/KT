#include <bits/stdc++.h>
using namespace std;
const int N = 90;
bool a[N];
int main() {
  int n;
  cin >> n;
  for (int i = 0, t; i < n; i++) {
    cin >> t;
    t--;
    a[t] = true;
  }
  int cnt = 0, time = 0;
  for (int i = 0; i < N && cnt < 15; i++) {
    if (a[i]) {
      time++;
      cnt = 0;
    } else {
      time++;
      cnt++;
    }
  }
  cout << time << endl;
  return 0;
}
