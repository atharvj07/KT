#include <bits/stdc++.h>

using namespace std;
int H, W;
string S;
int ans;

int main() {
  cin >> H >> W;

  for(int i = 0; i < H; i++) {
    cin >> S;
    for(int j = 0; j < S.length(); j++) if(S[j] == '#') ans++;
  }
  if(H+W-1 == ans) cout <<"Possible"<<endl;
  else cout << "Impossible" <<endl;
}

  
