#include<iostream>
#include<cctype>
#include<string>
#include<vector>
using namespace std;

vector<string> decompose(string s){
  vector<string> res;
  string tmp;
  tmp = s[0];
  
  for(int i=1;i<s.size();i++){
    if(isupper(s[i])){
      res.push_back(tmp);
      tmp = s[i];
    }else if(s[i] == '_'){
      res.push_back(tmp);
      tmp = "";
    }else{
      tmp += s[i];
    }
  }
  res.push_back(tmp);
  return res;
}

string unite(vector<string> v,char c){
  string res;

  for(int i=0;i<v.size();i++){
    if(c == 'D' || (c == 'L' && i==0)){
      v[i][0] = tolower(v[i][0]);
    }else{
      v[i][0] = toupper(v[i][0]);
    }

    if(c == 'D' && i!=0)res += "_";
    res += v[i];
  }
  return res;
}

int main(){
  string s;
  char c;

  while(cin >> s >> c, c!='X'){
    vector<string> v = decompose(s);
    cout << unite(v,c) << endl;
  }
}