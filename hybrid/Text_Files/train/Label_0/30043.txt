#include <bits/stdc++.h>
using namespace std;
const int MAX = (2e5) + 10;
pair<int, int> ara[MAX];
int id[MAX];
vector<int> didi[MAX];
void solve() {
  int n;
  cin >> n;
  for (int i = 0; i <= n - 1; i++) {
    cin >> ara[i].first;
  }
  for (int i = 0; i <= n - 1; i++) {
    cin >> ara[i].second;
  }
  sort(ara, ara + n, [](pair<int, int> x, pair<int, int> y) {
    return (x.first == y.first) ? x.second > y.second : x.first < y.first;
  });
  int cp = -1;
  priority_queue<int> que;
  long long sum, prin;
  sum = prin = 0;
  for (int i = 0; i <= n - 1; i++) {
    if (cp >= ara[i].first) {
      que.push(ara[i].second);
      sum += ara[i].second;
    } else {
      if (!que.empty()) {
        sum -= que.top();
        que.pop();
        prin += sum;
        cp++;
        i--;
      } else {
        cp = ara[i].first;
        i--;
      }
    }
  }
  while (!que.empty()) {
    sum -= que.top();
    que.pop();
    prin += sum;
  }
  cout << prin << endl;
}
int main() {
  ios::sync_with_stdio(false);
  int tc;
  solve();
  return 0;
}
