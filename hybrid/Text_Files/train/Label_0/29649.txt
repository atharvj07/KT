#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#define ll long long
using namespace std;
vector<pair<ll,ll>> sushi;
int N,K;
signed main(){
  cin >> N >> K;
  sushi.resize(N);
  for(int i = 0; i < N;i++){
    cin >> sushi[i].second >> sushi[i].first;
  }
  sort(sushi.begin(),sushi.end(),greater<pair<ll,ll>>());
  stack<ll> s;
  vector<bool> eaten(N + 1,false);
  ll typ = 0;
  ll sum = 0;
  for(int i = 0;i < K;i++){
    sum += sushi[i].first;
    if(not eaten[sushi[i].second]){
      typ++;
      eaten[sushi[i].second] = true;
    }
    else{
      s.emplace(sushi[i].first);
    }
  }

  ll ans = sum + typ * typ;
  for(int i = K;i<N;i++){
    sum += sushi[i].first;
    if(not eaten[sushi[i].second]){
      typ++;
      eaten[sushi[i].second] = true;
    }
    else{
      s.emplace(sushi[i].first);
    }

    if(s.empty()){
      break;
    }
    sum -= s.top();
    s.pop();
    ans = max(ans,sum + typ * typ);
  }
  cout << ans << endl;
  return 0;
}