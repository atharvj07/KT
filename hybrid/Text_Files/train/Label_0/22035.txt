#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  unordered_map<int, int> el_cnt, grp_cnt;
  for (int i = 0; i < n; i++) {
    int num;
    cin >> num;
    el_cnt[num]++;
    grp_cnt[el_cnt[num]]++;
  }
  int q;
  cin >> q;
  while (q--) {
    char typ;
    int num;
    cin >> typ >> num;
    if (typ == '+') {
      el_cnt[num]++;
      grp_cnt[el_cnt[num]]++;
    } else {
      grp_cnt[el_cnt[num]]--;
      el_cnt[num]--;
    }
    if (grp_cnt[8] > 0)
      cout << "YES" << endl;
    else if (grp_cnt[4] >= 2)
      cout << "YES" << endl;
    else if (grp_cnt[6] > 0 && grp_cnt[2] > 1)
      cout << "YES" << endl;
    else if (grp_cnt[4] > 0 && grp_cnt[2] >= 3)
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}
