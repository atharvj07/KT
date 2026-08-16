#include <iostream>
#include <string>

using namespace std;
int main(){
  string s;
  cin >> s;

  int n = s.length()-7;
  bool iFlg = false;
  for(int i=0;i<7;i++){
    string ans = s.substr(0, i) + s.substr(i+n);
    if(ans == "keyence"){
      iFlg = true;
      break;
    }
  }

  (iFlg)? ( cout << "YES"): (cout << "NO") << endl;

  return 0;
}