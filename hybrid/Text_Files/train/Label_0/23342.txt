#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

int n;
int in[5100];
unordered_set<int> vs;

int Solve(int x, int y) {
  int d = y - x;
  if (vs.count(x-d) > 0) return 0;
  int r = 1;
  for (int x = y; vs.count(x) > 0; x += d) {
    r++;
  }
  return r;
}

int main() {
  while (cin >> n) {
    vs.clear();
    for (int i = 0; i < n; ++i) {
      cin >> in[i];
      vs.insert(in[i]);
    }
    sort(in, in+n);
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i+1; j < n; ++j) {
        int r = Solve(in[i], in[j]);
        // cout << iter.first << " / " << r << endl;
        ans = max(ans, r);
      }
    }
    cout << ans << endl;
  }
}

