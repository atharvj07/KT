#include <bits/stdc++.h>
using namespace std;

string numstring(int i);

int main(){
  int m,n;

  while(1){
    cin >> m >> n;
    if(m == 0 && n == 0) break;


    vector<int> v;
    for(int i = 1;i <= m;i++) v.push_back(i);
    int pn = 0;

    string str[10000];
    for(int i = 0;i < n;i++){
      cin >> str[i];
    }

    for(int i = 1;i <= n;i++){
      string s;
      s = str[i-1];
      string ans;
      if(i % 3 == 0 && i % 5 == 0){
        ans = "FizzBuzz";
      }else if(i % 3 == 0){
        ans = "Fizz";
      }else if(i % 5 == 0){
        ans = "Buzz";
      }else{
        ans = numstring(i);
      }

      if(s == ans){
        pn = (pn + 1) % v.size();
      }else{
        v.erase(v.begin() + pn);
        if(pn == v.size()) pn = 0;
      }
      if(v.size() == 1) break;
    }

    for(int i = 0;i < v.size();i++){
      cout << v[i];
      if(i != v.size()-1) cout << " ";
    }
    cout << endl;
  }

  return 0;
}


char nums[10] = { '0','1','2','3','4','5','6','7','8','9' };

string numstring(int i){
  string ans;
  while(i > 0){
    ans.insert(ans.begin(),nums[i%10]);
    i = i/10;
  }

  return ans;
}


