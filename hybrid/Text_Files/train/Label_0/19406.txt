#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <queue>
#include <iomanip>
#include <set>
#include <tuple>
#define mkp make_pair
#define mkt make_tuple
#define rep(i,n) for(int i = 0; i < (n); ++i)
#define all(v) v.begin(),v.end()
using namespace std;
typedef long long ll;
const ll MOD=1e9+7;
template<class T> void chmin(T &a,const T &b){if(a>b) a=b;}
template<class T> void chmax(T &a,const T &b){if(a<b) a=b;}

struct SuffixArray{
    int N;
    vector<int> sa,rank;
    vector<int> ary;//int
    string str;//string

    SuffixArray(){}

    void build(const vector<int> &S){
        int k;//重要

        N=S.size();
        sa.resize(N+1,0);
        rank.resize(N+1,0);
        for(int i=0;i<=N;i++){
            sa[i]=i;
            rank[i]=(i<N ? S[i] : -1);
        }

        auto cmp = [&](int i,int j){
            if(rank[i]!=rank[j]) return rank[i]<rank[j];
            int ri=(i+k<=N ? rank[i+k] : -1);
            int rj=(j+k<=N ? rank[j+k] : -1);
            return ri<rj;
        };

        vector<int> tmp(N+1,0);
        for(k=1;k<=N;k*=2){
            sort(sa.begin(),sa.end(),cmp);

            tmp[sa[0]]=0;
            for(int i=1;i<=N;i++){
                tmp[sa[i]]=tmp[sa[i-1]]+(cmp(sa[i-1],sa[i]) ? 1 : 0);
            }
            rank=tmp;
        }

        //空文字を削除
        sa.erase(sa.begin());
        rank.pop_back();
        for(int i=0;i<rank.size();++i) --rank[i];
    }

    void initialize(const vector<int> &A){
        ary=A;
        build(A);
    }

    void initialize(const string &S){
        str=S;
        vector<int> A;
        for(int i=0;i<S.size();++i) A.push_back(S[i]);
        ary=A;
        build(A);
    }

    vector<int> lcp_array(const vector<int> &S,const vector<int> &sa){
        int N=S.size();
        vector<int> trans(N,0);
        for(int i=0;i<N;++i) trans[sa[i]]=i;

        vector<int> lcp(N-1,0);
        int len=0;
        for(int i=0;i<N;++i){
            len=max(0,len-1);
            int now=trans[i];
            if(now==N-1){
                len=0;
                continue;
            }

            int tar=sa[now+1];
            while(i+len<N&&tar+len<N){
                if(S[i+len]!=S[tar+len]) break;
                ++len;
            }
            lcp[now]=len;
        }
        return lcp;
    }

    int operator[](int i)const{
        return sa[i];
    }
};

int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);

  string S;
  cin>>S;
  ll N=S.size();

  SuffixArray SA;
  SA.initialize(S);
  vector<int> sa=SA.sa;

  ll ans=N*(N+1)/2;
  vector<int> lcp=SA.lcp_array(SA.ary,sa);
  for(auto x:lcp){
      ans-=x;
  }
  cout<<ans<<"\n";

  return 0;
}
