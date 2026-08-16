#include <iostream>
#include <string>

using namespace std;

int main(){
  string str;
  char code[6][5] = {{'a', 'b', 'c', 'd', 'e'},
                     {'f', 'g', 'h', 'i', 'j'},
                     {'k', 'l', 'm', 'n', 'o'},
                     {'p', 'q', 'r', 's', 't'},
                     {'u', 'v', 'w', 'x', 'y'},
                     {'z', '.', '?', '!', ' '}};
  while(cin >> str){
    if(str.size() % 2){
      cout << "NA\n";
      continue;
    }
    string ans = "";
    for(int i = 0; i < str.size(); i += 2){
      if(str[i] < '1' || '6' < str[i] || str[i + 1] < '1' || '5' < str[i + 1]){
        ans = "NA";
        break;
      }
      ans += code[str[i] - '1'][str[i + 1] - '1'];
    }
    cout << ans << "\n";
  }
  return 0;
}