#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  map<int, vector<int> > mm;
  for (int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;
    mm[a].push_back(b);
    mm[b].push_back(a);
  }
  for (map<int, vector<int> >::iterator it = mm.begin(); it != mm.end(); it++) {
    if ((it->second).size() == 1) {
      int an = it->first;
      cout << an;
      int act = (it->second)[0];
      while (mm[act].size() == 2) {
        cout << " " << act;
        int asd = act;
        if (mm[act][0] == an) {
          act = mm[act][1];
        } else {
          act = mm[act][0];
        }
        an = asd;
      }
      cout << " " << act << endl;
      break;
    }
  }
  return 0;
}
