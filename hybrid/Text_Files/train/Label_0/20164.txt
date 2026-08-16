#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

const long long INF = LLONG_MAX / 2;

int main()
{
    int t;
    cin >> t;

    while(--t >= 0){
        long long n;
        int e;
        cin >> n >> e;

        vector<vector<long long> > dp(51, vector<long long>(e+1, 0));
        for(int i=1; i<=50; ++i){
            for(int j=1; j<=e; ++j){
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + 1;
                dp[i][j] = min(dp[i][j], INF);
            }
        }

        int ans = 0;
        while(dp[ans][e] < n)
            ++ ans;
        cout << ans << endl;
    }

    return 0;
}