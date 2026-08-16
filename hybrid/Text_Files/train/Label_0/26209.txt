#include <bits/stdc++.h>
using namespace std;
void getIn(stack<int> &left, stack<int> &right,
           vector<pair<int, int>> &result) {
  while (!left.empty() && !right.empty()) {
    int lidx = left.top();
    left.pop();
    int ridx = right.top();
    right.pop();
    result.push_back({lidx, ridx});
  }
}
int main() {
  int n;
  cin >> n;
  string left, right;
  cin >> left >> right;
  map<char, stack<int>> leftIdx;
  map<char, stack<int>> rightIdx;
  for (int i = 0; i < n; i++) leftIdx[left[i]].push(i);
  for (int i = 0; i < n; i++) rightIdx[right[i]].push(i);
  vector<pair<int, int>> result;
  stack<int> lRemaining;
  stack<int> rRemaining;
  for (int i = 0; i < 26; i++) {
    char c = 'a' + i;
    getIn(leftIdx[c], rightIdx[c], result);
    while (!leftIdx[c].empty()) {
      int idx = leftIdx[c].top();
      leftIdx[c].pop();
      lRemaining.push(idx);
    }
    while (!rightIdx[c].empty()) {
      int idx = rightIdx[c].top();
      rightIdx[c].pop();
      rRemaining.push(idx);
    }
  }
  char qs = '?';
  getIn(leftIdx[qs], rRemaining, result);
  getIn(lRemaining, rightIdx[qs], result);
  getIn(leftIdx[qs], rightIdx[qs], result);
  cout << result.size() << endl;
  for (const auto &ans : result) {
    cout << ans.first + 1 << " " << ans.second + 1 << endl;
  }
}
