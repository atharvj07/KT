#include <bits/stdc++.h>
using namespace std;

const int64_t MOD=1000000007;

int main(){
  int N;
  cin>>N;
  
  int64_t ans=1;
  map<int64_t,int64_t> S;
  for(int i=0;i<N;++i){
    int64_t a;
    cin>>a;
    if(a==0){
      ans = ans*(3-S[0])%MOD;
      ++S[0];
    }
    else{
      ans = ans*(S[a-1]-S[a])%MOD;
      ++S[a];
    }
  }
  
  cout<<ans<<endl;
}