#include <bits/stdc++.h>
using namespace std;
int n, k;
bool a[2042];
int minTo[2042];
priority_queue<pair<int, int> > q;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n >> k;
  for (int i = 0; i < k; i++) {
    int b;
    cin >> b;
    a[1000 + (n - b)] = 1;
  }
  for (int i = 0; i <= 2000; i++) {
    minTo[i] = (1 << 20);
    if (a[i]) {
      q.push(make_pair(-1, i));
    }
  }
  for (; !q.empty();) {
    int val = -q.top().first, ind = q.top().second;
    q.pop();
    if (minTo[ind] != (1 << 20)) {
      continue;
    }
    minTo[ind] = val;
    for (int i = 0; i <= 2000; i++) {
      if (a[i] && ind + i - 1000 >= 0 && ind + i - 1000 <= 2000 &&
          minTo[ind + i - 1000] == (1 << 20)) {
        q.push(make_pair(-(val + 1), ind + i - 1000));
      }
    }
  }
  if (minTo[1000] == (1 << 20)) {
    cout << "-1\n";
    return 0;
  }
  cout << minTo[1000] << "\n";
  return 0;
}
