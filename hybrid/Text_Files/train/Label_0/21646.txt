#include <bits/stdc++.h>
using namespace std;
const int INF = 1 << 29;
const int xam = 100010;
int n, m;
string str[xam];
map<string, int> M;
vector<int> graf[xam];
pair<int, pair<int, int> > prize[xam];
vector<int> lisc;
vector<int> sorts[40];
string dane[40];
bool num[xam][40];
void set_ans() {
  bool bol = 0;
  for (typeof((sorts[1]).begin()) it = (sorts[1]).begin();
       it != (sorts[1]).end(); it++) {
    if (prize[*it].first == 1) {
      bol = 1;
      break;
    }
  }
  if (bol) {
    cout << "First\n";
    int maxi = 0, mini = INF;
    for (typeof((sorts[1]).begin()) it = (sorts[1]).begin();
         it != (sorts[1]).end(); it++) {
      if (prize[*it].first == 0) continue;
      if (prize[*it].second.first > maxi) {
        maxi = prize[*it].second.first;
        mini = prize[*it].second.second;
      } else if (prize[*it].second.first == maxi &&
                 prize[*it].second.second < mini) {
        maxi = prize[*it].second.first;
        mini = prize[*it].second.second;
      }
    }
    cout << maxi << " " << mini << "\n";
  } else {
    cout << "Second\n";
    int maxi = 0, mini = INF;
    for (typeof((sorts[1]).begin()) it = (sorts[1]).begin();
         it != (sorts[1]).end(); it++) {
      if (prize[*it].second.first > maxi) {
        maxi = prize[*it].second.first;
        mini = prize[*it].second.second;
      } else if (prize[*it].second.first == maxi &&
                 prize[*it].second.second < mini) {
        maxi = prize[*it].second.first;
        mini = prize[*it].second.second;
      }
    }
    cout << maxi << ' ' << mini << '\n';
  }
}
pair<int, pair<int, int> > set_prize(int a) {
  int mini = INF, maxi = 0;
  bool bol[2] = {0, 0};
  for (typeof((graf[a]).begin()) it = (graf[a]).begin(); it != (graf[a]).end();
       it++) {
    bol[prize[*it].first] = 1;
  }
  if (bol[1] == 1) {
    for (typeof((graf[a]).begin()) it = (graf[a]).begin();
         it != (graf[a]).end(); it++) {
      if (prize[*it].first == 0) continue;
      if (prize[*it].second.first > maxi) {
        maxi = prize[*it].second.first;
        mini = prize[*it].second.second;
      } else if (prize[*it].second.first == maxi &&
                 prize[*it].second.second < mini) {
        maxi = prize[*it].second.first;
        mini = prize[*it].second.second;
      }
    }
    return make_pair(0, make_pair(mini + prize[a].second.first, maxi));
  } else {
    for (typeof((graf[a]).begin()) it = (graf[a]).begin();
         it != (graf[a]).end(); it++) {
      if (prize[*it].second.first > maxi) {
        maxi = prize[*it].second.first;
        mini = prize[*it].second.second;
      } else if (prize[*it].second.first == maxi &&
                 prize[*it].second.second < mini) {
        maxi = prize[*it].second.first;
        mini = prize[*it].second.second;
      }
    }
    return make_pair(1, make_pair(mini + prize[a].second.first, maxi));
  }
}
void set_wyn() {
  for (int i = 39; i > 0; i--) {
    for (typeof((sorts[i]).begin()) it = (sorts[i]).begin();
         it != (sorts[i]).end(); it++) {
      if (prize[*it].first == -1) prize[*it] = set_prize(*it);
    }
  }
}
int score(string &s, int a) {
  int wyn = 0, maxi = 0;
  for (typeof((s).begin()) it = (s).begin(); it != (s).end(); it++) {
    maxi = max(maxi, (*it) - 'a' + 1);
    wyn += (*it - 'a' + 1);
  }
  wyn *= maxi;
  for (int i = 0; i < (n); i++) wyn += num[a][i];
  return wyn;
}
void set_sorts() {
  for (int i = 1; i <= (m); i++) {
    sorts[str[i].size()].push_back(i);
  }
  for (int i = 1; i <= (m); i++) prize[i].first = -1;
  for (int i = 1; i <= (m); i++) {
    prize[i] = make_pair(-1, make_pair(score(str[i], i), 0));
    if (!graf[i].size()) prize[i].first = 1;
  }
}
void set_graf() {
  string temp;
  map<string, int>::iterator p;
  for (int i = 1; i <= (m); i++) {
    temp = string("a") + str[i];
    for (int j = 'a'; j <= 'z'; j++) {
      temp[0] = j;
      p = M.find(temp);
      if (p == M.end()) continue;
      graf[i].push_back(p->second);
    }
    temp = str[i] + string("a");
    for (int j = 'a'; j <= 'z'; j++) {
      temp[temp.size() - 1] = j;
      p = M.find(temp);
      if (p == M.end()) continue;
      graf[i].push_back(p->second);
    }
  }
}
void read() {
  string temp;
  map<string, int>::iterator p;
  cin >> n;
  for (int i = 0; i < (n); i++) {
    cin >> dane[i];
    for (int j = 1; j <= (dane[i].size()); j++) {
      for (int l = 0; l < (dane[i].size() - j + 1); l++) {
        temp = dane[i].substr(l, j);
        p = M.find(temp);
        if (p == M.end()) {
          m++;
          M[temp] = m;
          str[m] = temp;
          num[m][i] = 1;
        } else
          num[p->second][i] = 1;
      }
    }
  }
}
int main() {
  read();
  set_graf();
  set_sorts();
  set_wyn();
  set_ans();
  return 0;
}
