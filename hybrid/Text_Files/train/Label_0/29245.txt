#include <bits/stdc++.h>
#define x first
#define y second
using namespace std;
typedef pair <int,int> P;
string mp[501];
int m,n,used[26],ans;
vector <P>  a[26];

int saiki(int);

bool check(int c,int s,int t,int f){
  int res=1;
  for(int i=s+1;i<t;i++){
    if(!f&&mp[i][c]!='.'&&!saiki(mp[i][c]-'A'))res=0;
    if(f&&mp[c][i]!='.'&&!saiki(mp[c][i]-'A'))res=0;
  }
  return res;
}

int saiki(int ch){
  int x1=a[ch][0].x,x2=a[ch][1].x;
  int y1=a[ch][0].y,y2=a[ch][1].y;
  int res=0;
  if(used[ch])return 0;
  used[ch]=1;
  
  if(x1==x2&&y2-y1!=1) res=check(x1,y1,y2,0);
  if(y1==y2&&x2-x1!=1) res=check(y1,x1,x2,1);
  
  if(x1!=x2&&y1!=y2) {
    if(x1<x2){
      res=check(y1,x1,x2+1,1)&check(x2,y1,y2,0);
      res|=check(x1,y1,y2+1,0)&check(y2,x1,x2,1);
    }
    else{
      swap(x1,x2);
      res=check(y1,x1-1,x2,1)&check(x1,y1,y2,0);
      res|= check(x2,y1,y2,0)&check(y2,x1,x2+1,1);
      swap(x1,x2);
    }
  }
  
  if(res) {
    mp[y1][x1]=mp[y2][x2]='.';
    a[ch].clear();
    ans+=2;
  }
  return res;
}

int main(){
  
  cin>>m>>n;
  for(int i=0;i<m;i++)cin>>mp[i];
  
  for(int i=0;i<m;i++)
    for(int j=0;j<n;j++)
      if(mp[i][j]!='.')a[mp[i][j]-'A'].push_back(P(j,i));
  
 
  int f=1;
  while(f--) 
    for(int i=0;i<26;i++){
       memset(used,0,sizeof(used));
      if(a[i].size()) f|=saiki(i);
  }
  cout<<ans<<endl;
  return 0;
}