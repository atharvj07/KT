#include <bits/stdc++.h>
using namespace std;

#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repl(i,0,n)
#define INF INT_MAX/3

#define fi first
#define se second

typedef long long ll;
typedef pair<int, int> P;

struct dice{
  int a[6];
};
void rot(int &a,int &b,int &c,int &d){
  int tmp=a; a=b; b=c; c=d; d=tmp;
}
void roll_f(dice &d){
  rot(d.a[0],d.a[3],d.a[2],d.a[1]);
}
void roll_b(dice &d){
  rot(d.a[0],d.a[1],d.a[2],d.a[3]);
}
void roll_l(dice &d){
  rot(d.a[3],d.a[5],d.a[1],d.a[4]);
}
void roll_r(dice &d){
  rot(d.a[3],d.a[4],d.a[1],d.a[5]);
}

typedef pair<P,int> pi;

int n;
map<P,int> nd[20];
ll dp[1<<15];

int main(int argc, char const *argv[]){
  while(1){
    cin>>n;
    if(n==0)break;
    rep(i,20)nd[i].clear();
    rep(i,1<<15){
      dp[i]=0;
    }
    rep(i,n){
      dice d;
      int sx,sy;
      string s;
      cin>>sx>>sy;
      cin>>d.a[4]>>d.a[5]>>d.a[0]>>d.a[2]>>d.a[1]>>d.a[3];
      cin>>s;
      nd[i][P(sx,sy)]=d.a[1];
      rep(j,s.length()){
        if(s[j]=='F'){
          roll_f(d);
          sy--;
        }
        if(s[j]=='B'){
          roll_b(d);
          sy++;
        }
        if(s[j]=='R'){
          roll_r(d);
          sx++;
        }
        if(s[j]=='L'){
          roll_l(d);
          sx--;
        }
        nd[i][P(sx,sy)]=d.a[1];
      }
    }
    rep(S,(1<<n)){
      map<P,bool> used;
      rep(i,n){
        if((S&(1<<i))==0)continue;
        for(auto it: nd[i]){
          used[it.fi]=true;
        }
      }
      rep(i,n){
        if((S&(1<<i))!=0)continue;
        ll add=0;
        for(auto it: nd[i]){
          if(used[it.fi])continue;
          add+=it.se;
        }
        int T=S|(1<<i);
        dp[T]=max(dp[T],dp[S]+add);
      }
    }
    cout<<dp[(1<<n)-1]<<endl;
  }
  return 0;
}