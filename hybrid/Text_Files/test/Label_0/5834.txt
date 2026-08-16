#include <bits/stdc++.h>
using namespace std;
string str;

bool sim(bool turn){

  int n = str.size();
  char pos = str[0];
  for(int i=1;i<n;i++){
    if(pos == str[i]) return 0;
    if(turn == 1 && str[i] == 'R') return 0;
    if(turn == 0 && str[i] == 'L') return 0;
    pos = str[i];
    turn = !turn;
  }
  return 1;
}

int main(){
  int q;
  cin>>q;
  while(q--){
  cin>>str;
  int ans = sim(0)|sim(1);
  cout<< (ans? "Yes":"No")<<endl;
  }
  

  return 0;  
}