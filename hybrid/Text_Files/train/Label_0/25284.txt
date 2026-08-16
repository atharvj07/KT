#include <bits/stdc++.h>
using namespace std;

int main(){
  string S;
  cin >> S;
  int x = S.size();
  
  string S_new;
  for(int i=0; i<8; i++){
    S_new = S;
    S_new.erase(i, x-7);
    if(S_new=="keyence"){
      cout << "YES";
      return 0;
    }
  }
  cout << "NO";
  return 0;
}