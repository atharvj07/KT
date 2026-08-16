#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef std::pair<int,int> pair2;
typedef std::pair<int,pair2> pair3;
const ll INF = 1LL<<60;
const  ll NUM=10e8+7;


int main(){
  ll N,X,M;
  cin>>N>>X>>M;
  
  ll ans=0;
  vector<ll> dist(M,-1);//カウント
 ll count;
  count=1;
while(1){
  //cout<<X;
  dist[X]=count;
  ans=ans+X;
  //cout<<"  "<<ans<<endl;
  if(count==N){cout<<ans<<endl;return 0;}
  X=(X*X)%M;
  //cout<<"  "<<X<<endl;
  count++;
  if(dist[X]!=-1){break;}
  }
//cout<<ans<<endl;
  ll cicle=count-dist[X];
  //cout<<cicle<<"."<<X<<endl;
  for(ll i=0;i<cicle;i++){
    ll num=(N-dist[X])/cicle;
    ans=ans+X*num;
    //cout<<X<<" "<<X*num<<endl;
    X=(X*X)%M;
  }
  cout<<ans<<endl;
}
