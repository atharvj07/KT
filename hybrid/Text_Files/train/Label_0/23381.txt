#include <bits/stdc++.h>
using namespace std;
map<string, int> mp;
map<int, string> mp_back;
vector<int> way[5005 * 2];
int n, j, i, ans[5005 * 2] = {};
int main() {
  cin >> n;
  int w = 0;
  for (i = 1; i <= n; i++) {
    int v1, v2;
    string s1, s2;
    cin >> s1 >> s2;
    if (!mp[s1])
      ++w, mp[s1] = w, v1 = w, mp_back[w] = s1;
    else
      v1 = mp[s1];
    if (!mp[s2])
      ++w, mp[s2] = w, v2 = w, mp_back[w] = s2;
    else
      v2 = mp[s2];
    way[v1].push_back(v2);
    way[v2].push_back(v1);
  }
  for (i = 1; i <= w; i++) {
    int friends[5005 * 2] = {}, friends2[5005 * 2] = {};
    for (j = 0; j < way[i].size(); j++) friends[way[i][j]] = 1;
    int maxf = 0;
    for (j = 1; j <= w; j++)
      if (!friends[j] && j != i) {
        int size = 0;
        for (int h = 0; h < way[j].size(); h++)
          if (friends[way[j][h]]) ++size;
        maxf = max(maxf, size);
        friends2[j] = size;
      }
    for (j = 1; j <= w; j++)
      if (friends2[j] == maxf && !friends[j] && j != i) ans[i]++;
  }
  cout << w << endl;
  for (i = 1; i <= w; i++) cout << mp_back[i] << " " << ans[i] << endl;
  return 0;
}
