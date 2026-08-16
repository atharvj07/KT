#include <bits/stdc++.h>
using namespace std;
int n, maxscore, minscore;
int main() {
  cin >> n;
  cin >> maxscore;
  minscore = maxscore;
  int ans = 0;
  for (int i = 1; i < n; i++) {
    int score;
    cin >> score;
    if (score > maxscore || score < minscore) {
      ans++;
      maxscore = max(maxscore, score);
      minscore = min(minscore, score);
    }
  }
  cout << ans << "\n";
  return 0;
}
