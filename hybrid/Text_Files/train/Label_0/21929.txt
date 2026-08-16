#include <bits/stdc++.h>
using namespace std;
int main(){
  string S;
  cin >> S;
  int w;
  cin >> w;
  for (int i = 0; i < S.size(); i++){
    if (i % w == 0){
      cout << S[i];
    }
  }
}