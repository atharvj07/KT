#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

typedef pair<int,int> pii;

int main(){
    int n, t;
    cin >> n >> t;
    vector<pii> v;
    for(int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;
        v.push_back({a,b});
    }
    sort(v.begin(), v.end());
    vector<int> dp(6005, 0);
    int ans = 0;
    for(int i = 0; i < n; i++){
        ans = max(ans, v[i].second+dp[t-1]);
        for(int j = t-1; j-v[i].first >= 0; j--){
            dp[j] = max(dp[j], dp[j-v[i].first]+v[i].second);
        }
    }
    cout << ans << endl;
    return 0;
}
