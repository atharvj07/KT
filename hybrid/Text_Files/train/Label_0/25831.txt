#include <bits/stdc++.h>
using namespace std;
int main(){
  while (1){
    int n;
    cin >> n;
    if (n == 0){
      break;
    }
    vector<string> s(n);
    for (int i = 0; i < n; i++){
      cin >> s[i];
      s[i] += '{';
    }
    vector<set<int>> E(26);
    bool ok = true;
    for (int i = 0; i < n - 1; i++){
      if (s[i] != s[i + 1]){
        int c = 0;
        while (s[i][c] == s[i + 1][c]){
          c++;
        }
        if (s[i + 1][c] == '{'){
          ok = false;
        } else if (s[i][c] != '{'){
          E[s[i][c] - 'a'].insert(s[i + 1][c] - 'a');
        }
      }
    }
    if (!ok){
      cout << "no" << endl;
    } else {
      vector<int> deg(26, 0);
      for (int i = 0; i < 26; i++){
        for (int j : E[i]){
          deg[j]++;
        }
      }
      queue<int> Q;
      for (int i = 0; i < 26; i++){
        if (deg[i] == 0){
          Q.push(i);
        }
      }
      while (!Q.empty()){
        int v = Q.front();
        Q.pop();
        for (int w : E[v]){
          deg[w]--;
          if (deg[w] == 0){
            Q.push(w);
          }
        }
      }
      for (int i = 0; i < 26; i++){
        if (deg[i] != 0){
          ok = false;
        }
      }
      if (!ok){
        cout << "no" << endl;
      } else {
        cout << "yes" << endl;
      }
    }
  }
}
