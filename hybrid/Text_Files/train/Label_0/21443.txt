#include <bits/stdc++.h>
using namespace std;
const long long mod = 1e7 + 7;
int main() {
  long long n, q1;
  cin >> n >> q1;
  queue<pair<int, int>> q;
  vector<int> timer(n + 1), mapi(n + 1);
  int total = 0, count = 0;
  vector<int> inValid(n + 1);
  while (q1--) {
    int x1, x2;
    cin >> x1 >> x2;
    if (x1 == 1) {
      q.push({x2, ++timer[x2]});
      total++;
      mapi[x2]++;
    } else if (x1 == 2) {
      total -= mapi[x2];
      mapi[x2] = 0;
      inValid[x2] = timer[x2];
    } else {
      if (count < x2) {
        for (int i = 0; i < x2 - count; ++i) {
          if (q.empty()) continue;
          int x = q.front().first;
          int y = q.front().second;
          q.pop();
          if (y > inValid[x] && mapi[x] > 0) {
            mapi[x]--;
            total--;
          }
        }
        count = x2;
      }
    }
    cout << total << endl;
  }
}
