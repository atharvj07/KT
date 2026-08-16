#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
const int inf = 2e9;

int ipow(int a, int p){
    int res = 1;
    for(int i=0; i<p; i++){
        res *= a;
    }
    return res;
}

int main(){
    while(1){
        int n,m;
        cin >> n >> m;
        if(n == 0) break;

        vector<int> a(n),w(m);
        for(int i=0; i<n; i++){
            cin >> a[i];
        }
        for(int i=0; i<m; i++){
            cin >> w[i];
        }
        set<int> diff;
        for(int i=0; i<ipow(3, m); i++){
            int tmp = i;
            int b[3] = {};
            for(int j=0; j<m; j++){
                b[tmp%3] += w[j];
                tmp /= 3;
            }
            diff.insert(abs(b[1]-b[0]));
        }

        vector<int> b;
        for(int i: a){
            if(diff.find(i) == diff.end()){
                b.push_back(i);
            }
        }
        if(b.empty()){
            cout << 0 << endl;
            continue;
        }
        int ans = inf;
        for(int e: diff){
            for(int s=-1; s<2; s+=2){
                int d = abs(b[0]+s*e);
                bool ok = true;
                for(int i: b){
                    if(diff.find(abs(i-d)) == diff.end() and diff.find(i+d) == diff.end()){
                        ok = false;
                        break;
                    }
                }
                if(ok){
                    ans = min(ans, d);
                }
            }
        }
        if(ans == inf){
            cout << -1 << endl;
        }else{
            cout << ans << endl;
        }
    }
    return 0;
}
