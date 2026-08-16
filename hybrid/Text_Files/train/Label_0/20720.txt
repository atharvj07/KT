#include<bits/stdc++.h>
using namespace std;
using Int = long long;
Int lim;
void fin(){
  cout<<"Error"<<endl;
  exit(0);
}

vector<Int> len({-1}), pos(26,0);
struct st{
  char c;
  Int v;
  st(char c):c(c),v(-1){}
};

const int D = 0;

st expr(string &s,Int &p);
st assign(string &s,Int &p);
st malloc(string &s,Int &p);
void free(string &s,Int &p);
st clone(string &s,Int &p);
st variable(string &s,Int &p);
Int number(string &s,Int &p);

void line(string &s,Int &p){
  if(s[0]=='f') free(s,p);
  else          expr(s,p);
}

st expr(string &s,Int &p){
  if(s[p]=='('){
    p++;
    st t=expr(s,p);
    if(D) assert(s[p]==')');
    p++;
    return t;
  }
  if(s[p]=='m'){
    return malloc(s,p);
  }
  if(s[p]=='c'){
    return clone(s,p);
  }
  if(p+1<(Int)s.size()&&isupper(s[p])&&s[p+1]=='='){
    return assign(s,p);
  }
  if(p+3<(Int)s.size()&&s[p]=='N'&&s[p+1]=='U'&&s[p+2]=='L'&&s[p+3]=='L'){
    return st('A'-1);
  }
  return variable(s,p);
}
st assign(string &s,Int &p){
  st t(s[p++]);
  if(D) assert(s[p]=='=');
  p++;
  t.v=expr(s,p).v;
  pos[t.c-'A']=t.v;
  return t;
}
st malloc(string &s,Int &p){
  if(D) assert(s[p]=='m');p++;
  if(D) assert(s[p]=='a');p++;
  if(D) assert(s[p]=='l');p++;
  if(D) assert(s[p]=='l');p++;
  if(D) assert(s[p]=='o');p++;
  if(D) assert(s[p]=='c');p++;
  if(D) assert(s[p]=='(');p++;
  Int res=number(s,p);
  if(D) assert(s[p]==')');p++;
  st t('A'-1);
  if(lim>=res){
    t.v=len.size();
    len.emplace_back(res);
    lim-=res;
  }else{
    t.v=-1;
  }
  return t;
}

void free(string &s,Int &p){
  if(D) assert(s[p]=='f');p++;
  if(D) assert(s[p]=='r');p++;
  if(D) assert(s[p]=='e');p++;
  if(D) assert(s[p]=='e');p++;
  if(D) assert(s[p]=='(');p++;
  st t=expr(s,p);
  if(D) assert(s[p]==')');p++;
  if(t.v<0) return;
  if(len[t.v]<0) fin();
  lim+=len[t.v];
  len[t.v]=-1;
}

st clone(string &s,Int &p){
  if(D) assert(s[p]=='c');p++;
  if(D) assert(s[p]=='l');p++;
  if(D) assert(s[p]=='o');p++;
  if(D) assert(s[p]=='n');p++;
  if(D) assert(s[p]=='e');p++;
  if(D) assert(s[p]=='(');p++;
  Int x=expr(s,p).v;
  if(D) assert(s[p]==')');p++;

  st t('A'-1);
  if(x<0) return t;
  Int res=len[x];
  if(res<0) fin();
  
  if(lim>=res){
    t.v=len.size();
    len.emplace_back(res);
    lim-=res;
  }else{
    t.v=-1;
  }
  
  return t;
  
}
st variable(string &s,Int &p){
  st t(s[p++]);
  t.v=pos[t.c-'A'];
  return t;
}
Int number(string &s,Int &p){
  Int res=0;
  while(isdigit(s[p]))
    res=res*10+(s[p++]-'0');
  return res;
}


signed main(){  
  cin.tie(0);
  ios::sync_with_stdio(0);
  cin>>lim;
  string s;
  while(cin>>s){
    Int p=0;
    line(s,p);
  }
  
  Int ans=0;
  for(Int i=0;i<26;i++) if(~pos[i]) len[pos[i]]=0;
  for(Int x:len) if(x>0) ans+=x;
  cout<<ans<<endl;
  return 0;
}

