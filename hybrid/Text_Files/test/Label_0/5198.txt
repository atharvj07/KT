#include <bits/stdc++.h>
#define int long long
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define F first
#define S second

using namespace std;
typedef pair<int,int> P;
typedef vector<int> ivec;

const int MOD=1000000007;
int INF=100100100100100;
int beki(int n){
  if(n==0)return 1;
  int x=beki(n/2);
  if(n%2==0)return x*x;
  return 2*x*x;
}
int a[310];
signed main(){
  int n;cin>>n;
  int c=0;
  rep(i,n)cin>>a[i];
  int x=a[0],y=a[1];
  for(int i=2;i<n;i++)c^=a[i];
  
  if(c>x+y || (x+y-c)%2!=0){
    cout<<-1<<endl;
    return 0;
  }
  int po=(x+y-c)/2;
  if((po & c)!=0){
    cout<<-1<<endl;
    return 0;
  }
  if(y<po)x-=(po-y),y=po;
  if(x<po){
    cout<<-1<<endl;
    return 0;
  }
  x-=po,y-=po;
  //cout<<x<<" "<<y<<" "<<po<<endl; 
  int res=0;
  for(int i=60;i>=0;i--){
    int nue=beki(i);
    int hoge=(x+y)/nue;
    if(hoge%2==1 && res+nue<=x)res+=nue;
  }
  //cout<<res<<endl;
  if(po+res==0){
    cout<<-1<<endl;
    return 0;
  }
  cout<<a[0]-po-res<<endl;
    
  return 0;
}