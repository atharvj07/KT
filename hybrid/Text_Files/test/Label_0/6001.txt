#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  vector<pair<long long int, long long int> > res(n);
  for (int i = 0; i < n; i++) {
    cin >> res[i].second >> res[i].first;
  }
  sort(res.begin(), res.end());
  long long int result;
  result = res[n - 1].second;
  long long int turn = res[n - 1].first;
  int i = n - 2;
  while (turn && i >= 0) {
    turn = turn - 1 + res[i].first;
    result += res[i].second;
    i--;
  }
  cout << result;
}
