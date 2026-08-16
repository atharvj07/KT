#include <bits/stdc++.h>
using namespace std;
#pragma comment(linker, "/stack:16000000")
#pragma warning(disable : 4996)
const int inf = 1 << 25;
const double eps = 1e-9;
int main(int argc, char* argv[]) {
  int n;
  cin >> n;
  int rs = 0;
  rs = n / 2;
  vector<pair<int, int> > ans;
  for (int u = (0); u < (rs); ++u)
    for (int v = (rs); v < (n); ++v)
      ans.push_back(pair<int, int>(u + 1, v + 1));
  cout << ans.size() << endl;
  for (int i = (0); i < ((int)ans.size()); ++i)
    printf("%d %d\n", ans[i].first, ans[i].second);
  return 0;
}
