#include <bits/stdc++.h>
using namespace std;
int dp[105][105][105], n;
vector<int> pilesNumbers[105];
set<pair<int, int> > s[2];
int getMaxDiff(int p, vector<pair<int, int> > indices, bool turn) {
  int i, j, res = INT_MIN, curr;
  if (~dp[p][indices[p].first][indices[p].second])
    return dp[p][indices[p].first][indices[p].second];
  bool doit = false;
  pair<int, int> b;
  for (i = 0; i < n; i++) {
    if (indices[i].first <= indices[i].second) {
      vector<pair<int, int> > tmpIndices = indices;
      if (turn)
        j = indices[i].first, tmpIndices[i].first = j + 1;
      else
        j = indices[i].second, tmpIndices[i].second = j - 1;
      if (j >= 0 && j < pilesNumbers[i].size()) {
        doit = true;
        curr = pilesNumbers[i][j] - getMaxDiff(i, tmpIndices, !turn);
        if (res < curr) res = curr, b = pair<int, int>(i, j);
      }
    }
  }
  if (!doit)
    res = 0;
  else
    s[turn].insert(b);
  return dp[p][indices[p].first][indices[p].second] = res;
}
int main() {
  int sum, diff, i, j, m, num, a, b, turn;
  vector<pair<int, int> > indices;
  vector<int> rems;
  scanf("%d", &n);
  a = b = 0;
  for (j = 0; j < n; j++) {
    scanf("%d", &m);
    for (i = 0; i < m; i++) {
      scanf("%d", &num);
      if (i < m / 2)
        a += num;
      else if ((m % 2 == 1) && (i == m / 2))
        rems.push_back(num);
      else
        b += num;
    }
  }
  sort((rems).begin(), (rems).end(), greater<int>());
  turn = 1;
  for (i = 0; i < rems.size(); i++) {
    if (turn)
      a += rems[i];
    else
      b += rems[i];
    turn = 1 - turn;
  }
  printf("%d %d\n", a, b);
  return 0;
}
