#include <bits/stdc++.h>

using namespace std;

char j_s_board[10][10];
int idx,width;

int jtos(string jfen){
  std::vector<char> board[10];
  int len=jfen.length();
  idx=0;width=0;
  for(int i=0;i<len;i++){
    if(jfen[i]=='/') idx++;
    else{
      if(jfen[i]=='b'){
        board[idx].push_back('b');
        width++;
      }
      else{
        int j=jfen[i]-'0';
        for(int k=0;k<j;k++){
          board[idx].push_back('.');
          width++;
        }
      }
    }
  }
  for(int i=0;i<idx+1;i++) for(int j=0;j<width/(idx+1);j++) j_s_board[i][j]=board[i][j];
  return 0;
}

string stoj(){
  string res="";
  for(int i=0;i<idx+1;i++){
    char num='0';//.?????£?¶?????????°
    for(int j=0;j<width/(idx+1);j++){
      if(j_s_board[i][j]=='.') num++;
      else{
        if(num!='0') res+=num;
        res+='b';
        num='0';
      }
    }
    if(num!='0') res+=num;
    if(i<idx) res+="/";
  }
  return res;
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);

  string jfen;
  while(cin>>jfen,jfen!="#"){
  jtos(jfen);
  int a,b,c,d;cin>>a>>b>>c>>d;
  char tmp=j_s_board[a-1][b-1];
  j_s_board[a-1][b-1]=j_s_board[c-1][d-1];
  j_s_board[c-1][d-1]=tmp;
  string ans=stoj();
  cout<<ans<<endl;
}
}