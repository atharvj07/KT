#include <bits/stdc++.h>
using namespace std;




int main(){
  int n;
  cin>>n;
  vector<string> s;
  for(int i=0;i<n;i++){
    string a;
    cin>>a;
    s.push_back(a);
  }
  for(int i=s.size()-1;i>=0;i-=2){
    cout << s.at(i)<< " ";
  }
  int k;
  if(n%2==0){
    k=0;
  }
  else{
    k=1;
  }
  for(int j=k;j<s.size();j+=2){
    cout << s.at(j)<< " ";
  }
}