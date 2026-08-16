#include <bits/stdc++.h>
using namespace std;
map<int, int> cost, sum;
int H;
void add(int v, int e) {
  cost[v] += e;
  for (; v >= 1; v /= 2) sum[v] += e;
}
double expectation(int depth, int v, double potential) {
  if (depth == H) return max(potential, 1.0 * cost[v]);
  int left = sum[2 * v], right = sum[2 * v + 1];
  double ans1 = max(potential, 1.0 * cost[v] + left);
  if (right > cost[v] + left && right > ans1)
    ans1 = expectation(depth + 1, 2 * v + 1, ans1);
  double ans2 = max(potential, 1.0 * cost[v] + right);
  if (left > cost[v] + right && left > ans2)
    ans2 = expectation(depth + 1, 2 * v, ans2);
  return (ans1 + ans2) / 2.0;
}
int main() {
  const string _add = "add";
  const string _decay = "decay";
  int q, v, e;
  string command;
  cin >> H >> q;
  for (int _n(q), request(0); request < _n; request++) {
    cin >> command;
    if (command == _add) {
      cin >> v >> e;
      add(v, e);
    } else {
      cout << expectation(0, 1, 0) << endl;
    }
  }
  return 0;
}
