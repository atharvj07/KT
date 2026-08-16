#include <bits/stdc++.h>
using namespace std;
using ll = long long;
template <class T> using vec = vector<T>;
template <class T> using vvec = vector<vec<T>>;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int N,M;
    while(cin >> N >> M && N){
        vec<int> S(N);
        set<int> s;
        for(auto& x:S) cin >> x;

        int inf = 1e9;
        auto calc = [&](int x){
            int cnt = 0;
            int now = 1;
            while(now+x<=S[N-1]){
                int ma = -1;
                auto it = upper_bound(S.begin(),S.end(),now);
                if(*it<now+x){
                    ma = max(1,x-abs(now-*it));
                }
                if(it!=S.begin()){
                    it--;
                    if(*it<now+x){
                        ma = max(ma,max(x-abs(now-*it),1));
                    }
                }
                if(ma==-1) return inf;
                cnt++;
                now += ma;
            }
            return cnt+1;
        };

        int mi = S[0];
        if(calc(mi)<M){
            cout << -1 << "\n";
            continue;
        }
//        cerr << calc(3) << "\n";
        int l = mi,r = S[N-1];
        while(l+1<r){
            int m = (l+r)/2;
            if(calc(m)>=M) l = m;
            else r = m;
        }
        cout << l << "\n";
    }
}

