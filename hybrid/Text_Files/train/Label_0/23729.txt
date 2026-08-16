#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=(int)(a);i < (int)(b);++i)
template<class T1, class T2> ostream& operator << (ostream &s, pair<T1,T2> P)
{ return s << '<' << P.first << ", " << P.second << '>'; }
template<class T> ostream& operator << (ostream &s, vector<T> P)
{ for (int i = 0; i < P.size(); ++i) { if (i > 0) { s << " "; } s << P[i]; } return s; }
template<class T> ostream& operator << (ostream &s, vector<vector<T> > P)
{ for (int i = 0; i < P.size(); ++i) { s << endl << P[i]; } return s << endl; }
template<class Key,class Value> ostream& operator << (ostream &s, map<Key,Value> M)
{ for ( auto itr = begin(M); itr != end(M); ++itr) { s << itr->first << ":" << itr->second; } return s;}
void print(const std::vector<int>& v)
{
  std::for_each(v.begin(), v.end(), [](int x) {
    std::cout << x << " ";
  });
  std::cout << std::endl;
}
bool is_sub(string s1,string s2) {
    int s1_size = s1.size();
    int s2_size = s2.size();
    if (s1_size > s2_size) {
        rep(i,s1_size-s2_size + 1) {
            bool flg = true;
            rep(j,s2_size) {
                if (s1[i+j] != s2[j]) {
                    flg = false;
                    break;
                }
            }
            if (flg) return true;
        }
        return false;
    }
    else {
        rep(i,s2_size-s1_size + 1) {
            bool flg = true;
            rep(j,s1_size) {
                if (s2[i+j] != s1[j]) {
                    flg = false;
                    break;
                }
            }
            if (flg) return true;
        }
        return false;
    }
}

int main() {
    while (true) {
        int n = 0;
        cin >> n;
        if (n == 0) {
            break;
        }
        long init = 0;
        vector<string> S(n);
        rep(i,n) cin >> S[i];
        rep(i,n-1) {
            repi(j,i+1,n) {
                // cout << is_sub(S[i],S[j]) << " " << i << " " << j << endl;
                if( is_sub(S[i],S[j]) ) {
                    if (S[i].size() > S[j].size()) init |= (1 << j);
                    else init |= (1 << i);
                }
            }
        }


        vector<int> v;
        rep(i,n) {
            if (!((init >> i) & 1)) v.push_back(i);
        }
        //cout << v << endl;
        // cout << v << endl;

        // suffix,prefix計算
        vector<vector<string>> preffix(n),suffix(n);
        rep(i,n) {
            if (((init >> i) & 1)) continue;
            preffix[i] = vector<string>(S[i].size()+1,"");
            suffix[i] = vector<string>(S[i].size()+1,"");
            rep(j, S[i].size()) {
                repi(k,j+1,S[i].size()+1) {
                    preffix[i][k] += S[i][j];
                    suffix[i][k] = S[i][S[i].size()-1-j] + suffix[i][k];
                }
            }
        }

        int string_num = v.size();
        string ans = "77";
        
        do {
            string cur = S[v[0]];
            rep(i, string_num-1) {
                int s_size = min(S[v[i]].size(),S[v[i+1]].size());
                rep(j,s_size) {
                    //cout << suffix[v[i]][s_size-1-j] << " " << preffix[v[i+1]][s_size-1-j] << endl;;
                    if (suffix[v[i]][s_size-1-j] == preffix[v[i+1]][s_size-1-j]) {
                        //cout << cur << " " << suffix[v[i+1]][S[v[i+1]].size()-j] << endl;
                        
                        int match = s_size - 1 - j;
                        cur += suffix[v[i+1]][S[v[i+1]].size()-match];
                        break;
                    }
                }
            }
            if (ans == "77" || ans.size() > cur.size() || ( ans.size() == cur.size() && ans > cur)) ans = cur;
        } while (next_permutation(v.begin(), v.end()));
        
        cout << ans << endl;


        

        
        
    }
}

