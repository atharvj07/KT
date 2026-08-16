#include <bits/stdc++.h>

using namespace std;

using i64 = int64_t;
const i64 MOD = 1e9 + 7;
const i64 INF = i64(1e18) + 7;

signed main(){
    int N;cin >> N;
    vector<double> vec;
    for(int i = 0;i < N;i++){
        int a;cin >> a;
        vec.push_back(a);
    }
    double ans = -1e9;
    sort(vec.begin(), vec.end());
    for(int i = 0;i < N-1;i++){
        for(int j = i+1;j < N;j++){
            int cnt = 0;
            double sum = 0;
            for(int k = N-1;k >= 0;k--){
                if(cnt >= 2)break;
                if(i == k || j == k){
                    continue;
                }else{
                    cnt++;
                    sum += vec[k];
                }
            }
            ans = max(ans, sum / (vec[j] - vec[i]));
        }
    }
    cout<<setprecision(20)<<ans<<endl;
}

