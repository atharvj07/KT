#include<bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(x) x.begin(),x.end()
#define dbg(x) cout<<#x<<":"<<x<<endl
typedef long long ll;
typedef pair<ll,ll> P;
typedef pair<ll,P> PP;

int main(){
  int h,w;
  vector<int> g[30];
  char s,t,a[50][50];
  cin>>h>>w>>s>>t;  
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      cin>>a[i][j];
    }
  }

  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      if('A'>=a[i][j]||a[i][j]>='Z')continue;
      
      int dx[4]={0,1,0,-1};
      int dy[4]={1,0,-1,0};
      for(int k=0;k<4;k++){
	int tx=i+dx[k],ty=j+dy[k];
	while(1){
	  if(tx<0||h<=tx||ty<0||w<=ty)break;
	  if(a[tx][ty]=='.')break;
	  if(k%2&&a[tx][ty]=='-')break;
	  if(k%2==0&&a[tx][ty]=='|')break;
	  if('A'<=a[tx][ty]&&a[tx][ty]<='Z'){
	    g[a[i][j]-'A'].pb(a[tx][ty]-'A');
	    g[a[tx][ty]-'A'].pb(a[i][j]-'A');
	    break;
	  }
	  tx+=dx[k],ty+=dy[k];
	}
      }
    }
  }

  queue<P>q;
  q.push(P(s-'A',0));
  int used[30]={};

  while(q.size()){
    int node=q.front().fi;
    int l=q.front().se;
    q.pop();
    if(node==t-'A'){
      cout<<l<<endl;
      return 0;
    }
    if(used[node])continue;
    used[node]=1;
    for(int i=0;i<g[node].size();i++){
      q.push(P(g[node][i],l+1));
    }
  }
  return 0;
}

