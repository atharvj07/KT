#include <bits/stdc++.h>
using namespace std;
class Solution {
 public:
  void solve(std::istream& in, std::ostream& out) {
    int n;
    in >> n;
    int ans = n / 2 + n % 2 - 1;
    out << ans << "\n";
  }
};
void solve(std::istream& in, std::ostream& out) {
  out << std::setprecision(12);
  Solution solution;
  solution.solve(in, out);
}
int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  istream& in = cin;
  ostream& out = cout;
  solve(in, out);
  return 0;
}
