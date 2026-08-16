#include <bits/stdc++.h>
using namespace std;
int N, M;
inline bool judge(int temp) {
  int x = temp / 2;
  int y = temp / 3;
  int z = temp / 6;
  if (x >= N && y >= M && x + y - z >= N + M) return 1;
  return 0;
}
int main() {
  int l = 0, r = 10000000;
  int ans;
  cin >> N >> M;
  while (l <= r) {
    int mid = (l + r) >> 1;
    if (judge(mid)) {
      ans = mid;
      r = mid - 1;
    } else
      l = mid + 1;
  }
  cout << ans << endl;
  return 0;
}
