#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9 + 7;
const int maxn = 7008;
long long int ans[2][maxn], arr[2][maxn], cnt[2][maxn];
int main() {
  ios_base::sync_with_stdio(false);
  long long int n, k[2], i;
  cin >> n;
  cin >> k[0];
  for (i = 0; i < k[0]; i++) cin >> arr[0][i];
  cin >> k[1];
  for (i = 0; i < k[1]; i++) cin >> arr[1][i];
  ans[1][0] = ans[0][0] = 2;
  queue<pair<long long int, long long int> > q;
  q.push(make_pair(1, 0));
  q.push(make_pair(0, 0));
  while (!q.empty()) {
    long long int player = q.front().first, position = q.front().second;
    q.pop();
    if (ans[player][position] == 2) {
      for (i = 0; i < k[1 ^ player]; i++) {
        long long int newPosition = (position - arr[1 ^ player][i] + n) % n;
        if (!ans[1 ^ player][newPosition]) {
          ans[1 ^ player][newPosition] = 1;
          q.push(make_pair(1 ^ player, newPosition));
        }
      }
    } else {
      for (i = 0; i < k[1 ^ player]; i++) {
        long long int newPosition = (position - arr[1 ^ player][i] + n) % n;
        if (!ans[1 ^ player][newPosition]) cnt[1 ^ player][newPosition]++;
        if (!ans[1 ^ player][newPosition] &&
            cnt[1 ^ player][newPosition] == k[1 ^ player]) {
          ans[1 ^ player][newPosition] = 2;
          q.push(make_pair(1 ^ player, newPosition));
        }
      }
    }
  }
  for (i = 1; i < n; i++) {
    if (ans[0][i] == 2)
      cout << "Lose ";
    else if (ans[0][i] == 1)
      cout << "Win ";
    else
      cout << "Loop ";
  }
  cout << endl;
  for (i = 1; i < n; i++) {
    if (ans[1][i] == 2)
      cout << "Lose ";
    else if (ans[1][i] == 1)
      cout << "Win ";
    else
      cout << "Loop ";
  }
  return 0;
}
