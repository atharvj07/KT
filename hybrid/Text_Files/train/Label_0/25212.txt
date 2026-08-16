#include <iostream>
using namespace std;
int main(){
  string s;
 

  while(cin >> s){
 int ans_JOI = 0,ans_IOI = 0;
    for(int i = 0 ; i < s.size() ; i++ ){
      if(s[i] == 'J' && s[i + 1] == 'O' && s[i + 2] == 'I')ans_JOI++;
      if(s[i] == 'I' && s[i + 1] == 'O' && s[i + 2] == 'I')ans_IOI++;
    }
  cout << ans_JOI << endl;
  cout << ans_IOI << endl;
  }
  return 0;
}