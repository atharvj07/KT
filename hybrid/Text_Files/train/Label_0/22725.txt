#include <bits/stdc++.h>
using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

typedef long long LL;

int main(){
  int n;
  cin >> n;
  string s;
  cin >> s;
  vector<int> Rr(n+1,0),Lr(n+1,0);
  for(int i=1;i<=n;i++){
    if(s[i-1]=='>'){
      Rr[i]=Rr[i-1]+1;
      Lr[i]=Lr[i-1];
    }else{
      Rr[i]=Rr[i-1];
      Lr[i]=Lr[i-1]+1;
    }
  }
  int ans=0;
  for(int i=1;i<=n;i++){
    if(s[i-1]=='>'){
      if(Rr[i]>Lr[n]-Lr[i]){
        ans=max(ans,n-(lower_bound(Rr.begin(),Rr.end(),Rr[i]-(Lr[n]-Lr[i]))-Rr.begin())+1);
        //cout << n-(lower_bound(Rr.begin(),Rr.end(),Rr[i]-(Lr[n]-Lr[i]))-Rr.begin())+1 << endl;
      }else{
        ans=max(ans,lower_bound(Lr.begin(),Lr.end(),Rr[i]+Lr[i])-Lr.begin());
        //cout << lower_bound(Lr.begin(),Lr.end(),Rr[i]+Lr[i])-Lr.begin() << endl;
      }
    }else{
      if(Rr[i-1]>=Lr[n]-Lr[i-1]){
        ans=max(ans,n-(lower_bound(Rr.begin(),Rr.end(),Rr[i-1]-(Lr[n]-Lr[i-1])+1)-Rr.begin()-1));
        //cout << n-(lower_bound(Rr.begin(),Rr.end(),Rr[i-1]-(Lr[n]-Lr[i-1])+1)-Rr.begin()-1) << endl;
      }else{
        ans=max(ans,lower_bound(Lr.begin(),Lr.end(),Rr[i-1]+Lr[i-1]+1)-Lr.begin());
        //cout << lower_bound(Lr.begin(),Lr.end(),Rr[i-1]+Lr[i-1]+1)-Lr.begin() << endl;
      }
    }
  }
  cout << ans << endl;
  return 0;
}

