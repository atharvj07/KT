#include <bits/stdc++.h>
using namespace std;
using ul=unsigned long long;
int s[500],t[500],tmp[500][500],S[500],T[500],n,bit=-1,IN;
ul ans[500][500],u[500],v[500];

void ng(){
  cout<<-1;
  exit(0);
}

struct P{int va,idx,ve,ne,al;};
bool operator <(const P&a,const P&b){return a.va<b.va;};
priority_queue<P>que;

#define REP(i) for(int i=0;i<n;i++)
#define U ((u[i]>>bit)&1)
#define V ((v[j]>>bit)&1)

#define F(va) {\
  if(!~tmp[i][j]){\
    ans[i][j]+=((ul)1<<bit)*(tmp[i][j]=va);\
    if(++S[i]<n&&IN)que.push({S[i],i,'S',s[i],1});\
    if(++T[j]<n&&IN)que.push({T[j],j,'T',t[j],1});\
  }\
}

void AL(){
  int koushin=1;
  while(koushin--){
    REP(i)
      if(s[i]==U){
        bool f=0;
        REP(j)f|=tmp[i][j]==s[i];
        if(f)REP(j){koushin|=tmp[i][j]<0;F(s[i]^1);}
      }
    REP(j)
      if(t[j]==V){
        bool f=0;
        REP(i)f|=tmp[i][j]==t[j];
        if(f)REP(i){koushin|=tmp[i][j]<0;F(t[j]^1);}
      }
  }
}

int main(){
  cin>>n;
  REP(i)cin>>s[i];
  REP(i)cin>>t[i];
  REP(i)cin>>u[i];
  REP(i)cin>>v[i];

  while(++bit<64){
    memset(tmp,-1,sizeof(tmp));
    memset(S,0,sizeof(S));
    memset(T,0,sizeof(T));
    IN=0;

    REP(i)if(s[i]^U)REP(j)F(s[i]^1);
    REP(j)if(t[j]^V)REP(i)F(t[j]^1);
    REP(i)REP(j)if(s[i]==U&&U==t[j]&&t[j]==V)F(s[i]);

    AL();
    IN=1;
    REP(i)if(S[i]<n)que.push({S[i],i,'S',s[i],1});
    REP(j)if(T[j]<n)que.push({T[j],j,'T',t[j],1});

    while(que.size()){
      P p=que.top();que.pop();
      if(p.ve=='S'){
        int i=p.idx;
        if(p.va<S[i])continue;
        REP(j)
          if(!~tmp[i][j]){
            F(p.ne);
            p.ne^=p.al;p.al=0;
          }
        AL();
      }
      else{
        int j=p.idx;
        if(p.va<T[j])continue;
        REP(i)
          if(!~tmp[i][j]){
            F(p.ne);
            p.ne^=p.al;p.al=0;
          }
        AL();
      }
    }
  }

  REP(i){
    ul A=ans[i][0];
    REP(j)
      if(s[i])A|=ans[i][j];
      else A&=ans[i][j];
    if(A!=u[i])ng();
  }
  REP(j){
    ul A=ans[0][j];
    REP(i)
      if(t[j])A|=ans[i][j];
      else A&=ans[i][j];
    if(A!=v[j])ng();
  }

  REP(i){
    REP(j)cout<<ans[i][j]<<" ";cout<<endl;
  }
}