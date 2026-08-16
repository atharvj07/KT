#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
  int n;
  string input;
  vector<int> result;

  cin>>n;

  for(int i=0;i<n;++i){
    int a,b;
    int s;
    
    cin>>input;

    sort(input.begin(),input.end(),greater<int>());
    a=stoi(input);

    sort(input.begin(),input.end());
    b=stoi(input);

    s=a-b;
    
    result.push_back(s);
  }

  for(auto i:result)
    cout<<i<<endl;

}