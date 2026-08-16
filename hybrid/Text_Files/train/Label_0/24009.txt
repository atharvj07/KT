#include<bits/stdc++.h>
using namespace std;
using Int = long long;
using ll = long long;

template<typename T1,typename T2> inline void chmin(T1 &a,T2 b){if(a>b)a=b;};
template<typename T1,typename T2> inline void chmax(T1 &a,T2 b){if(a<b)a=b;};

template<typename T, T MOD, T B>
struct RollingHash{
  vector<T> hash, p;
  RollingHash(){}
  RollingHash(const string &s){
    Int n = s.size();
    hash.assign(n+1, 0);
    p.assign(n+1, 1);
    for(Int i=0;i<n;i++){
      hash[i+1] = (hash[i] * B + s[i]) % MOD;
      p[i+1] = p[i] * B % MOD;
    }
  }

  //S[l , r)
  T find(Int l, Int r){
    T res = hash[r] + MOD - hash[l] * p[r - l] % MOD;
    return res >= MOD? res - MOD:res;
  }
};

const Int MOD = 1e9+7;
const Int B = 1777771;
using RH = RollingHash<Int, MOD, B>;
string pat;
RH base;

Int calc(string &s,string &t){
  Int res=0;
  Int n=s.size(),m=t.size();
  Int len=pat.size();
  if(n+m<len) return 0;
  
  RH rh(s+t);
  for(Int i=0;i<n&&i+len<=n+m;i++){
    if(i+len<=n) continue;
    if(rh.find(i,i+len)==base.find(0,len)) res++;
  }  
  return res;  
}

struct State{
  Int type,cnt;
  string all,lft,rgh;
  State(char c){
    type=0;
    cnt=0;
    all+=c;
    if(all==pat) cnt++;
  }
  
  State(){
    type=0;
    cnt=0;
  }
  
  void merge(State oth){    
    State res;
    res.cnt=cnt+oth.cnt;
    
    if(pat.size()!=1u){
      res.type=0;      
      if(type==0){
        if(oth.type==0){
          res.cnt+=calc(all,oth.all);
          
          res.all=all+oth.all;
          if(all.size()>=pat.size()){
            res.type=1;
            res.lft=res.all.substr(0,pat.size());
            res.rgh=res.all.substr(res.all.size()-pat.size());
            res.all.clear();
          }
        }else{
          res.cnt+=calc(all,oth.lft);

          res.type=1;
          res.lft=(all+oth.lft).substr(0,pat.size());
          res.rgh=oth.rgh;
        }
      }else{
        if(oth.type==0){
          res.cnt+=calc(rgh,oth.all);
          
          res.type=1;
          res.lft=lft;
          res.rgh=rgh+oth.all;
          res.rgh=res.rgh.substr(res.rgh.size()-pat.size());
        }else{
          res.cnt+=calc(rgh,oth.lft);
          
          res.type=1;
          res.lft=lft;
          res.rgh=oth.rgh;          
        }
      }          
    }    
    (*this)=res;
  }

  State repeat(Int num){
    if(num==1) return *this;
    num--;
    State res(*this),dbl(*this);   
    while(num){
      if(num&1) res.merge(dbl);
      dbl.merge(dbl);
      num>>=1;
    }
    //cout<<res.all<<":"<<res.lft<<" "<<res.rgh<<endl;
    return res;
  }
  
  State(char c,Int num){
    (*this)=State(c).repeat(num);
  }
};


State expr(string &s,Int &p);
State factor(string &s,Int &p);
State letter(string &s,Int &p);
Int number(string &s,Int &p);

const int DEBUG = 0;

State letter(string &s,Int &p){
  if(DEBUG) cout<<s<<":l:"<<p<<endl;
  assert(p<(Int)s.size()&&isupper(s[p]));
  return State(s[p++]);
}

Int number(string &s,Int &p){
  if(DEBUG) cout<<s<<":n:"<<p<<endl;
  Int res=0;
  while(p<(Int)s.size()&&isdigit(s[p])){
    res=res*10+(s[p]-'0');
    p++;
  }
  return res;
}

State expr(string &s,Int &p){
  if(DEBUG) cout<<s<<":e:"<<p<<endl;
  State res=factor(s,p);
  while(p<(Int)s.size()&&s[p]!=')'){
    State nxt=factor(s,p);
    res.merge(nxt);
  }
  return res;
}

State factor(string &s,Int &p){
  if(DEBUG) cout<<s<<";f;"<<p<<endl;
  if(isdigit(s[p])){
    Int num=number(s,p);
    if(isupper(s[p])) return State(s[p++],num);
    assert(s[p]=='(');
    p++;
    State res=expr(s,p);
    assert(s[p]==')');
    p++;
    return res.repeat(num);
  }
  return letter(s,p);
}

signed main(){
  cin.tie(0);
  ios::sync_with_stdio(0);

  string s;
  while(cin>>s,s!="#"){
    cin>>pat;
    base=RH(pat);
    Int p=0;
    State res=expr(s,p);
    //cout<<res.all<<endl;
    cout<<res.cnt<<endl;
  }  
  
  return 0;
}

