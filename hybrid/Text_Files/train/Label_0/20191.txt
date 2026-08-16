 
#include <bits/stdc++.h>
using namespace std;
using vi=vector<int>;
using vvi=vector<vi>;
using vs=vector<string>;
using msi=map<string,int>;
using mii=map<int,int>;
using pii=pair<int,int>;
using vlai=valarray<int>;
using ll=long long;
#define rep(i,n) for(int i=0;i<n;i++)
#define range(i,s,n) for(int i=s;i<n;i++)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define fs first
#define sc second
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define INF 1e9
#define EPS 1e-9

string solve(string s){
    int d=0,dep=0;
    string ans=s;
    stack<int> p;
    for(int i=0;i<s.size();i++){
        char c=s[i];
        if(c=='[') p.push(i);
        else if(c==']'){
            int f=p.top(),l; p.pop();
            string inner=s.substr(f+1,i-f-1);
            l=inner.length()+2;
            inner=solve(s.substr(f+1,i-f-1));
            reverse(all(inner));
            auto tmp=s.substr(0,f)+inner+s.substr(i+1);
            s=tmp;
            i-=l-inner.length();
        }
        else if(c=='+') d++,dep++;
        else if(c=='-') d--,dep++;
        else{
            char tt;
            if(c=='?')tt='A';
            else tt=(char)((c-'A'+d+2600)%26+'A');
            auto tmp=s.substr(0,i-dep)+tt+s.substr(i+1);
            i-=dep;
            s=tmp;
            d=dep=0;
        }
    }
    return s;
}

string bur(string s){
    // string ans(100,'Z');
    // if(count(all(s),'?')==0) return solve(s);
    // rep(i,26){
    //     string os=s;
    //     os[s.find('?')]='A'+i;
    //     ans=min(ans,bur(os));
    // }
    return solve(s);
}



int main(){
    string o;
    while(cin>>o,o!="."){
        cout<<bur(o)<<endl;
    }
	return 0;
}

