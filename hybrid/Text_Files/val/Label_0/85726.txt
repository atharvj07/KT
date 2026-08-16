#include <cstdio>
#include <iostream>
#include <sstream>
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
#include <climits>
#include <cfloat>
using namespace std;

int n;
vector<int> a;

string solve(int x, int v)
{
    if(v * v > x * (2 * a[n-1]))
        return "crash";

    x *= 2;
    vector<vector<bool> > dp(x+1, vector<bool>(v+1, false));
    dp[x][v] = true;

    for(int i=x; i>=0; --i){
        for(int j=v; j>=0; --j){
            if(!dp[i][j])
                continue;
            for(int k=0; k<n; ++k){
                int i2 = i - 2 * j + a[k];
                int j2 = j - a[k];
                if(i2 >= 0 && j2 >= 0)
                    dp[i2][j2] = true;
            }
        }
    }

    if(dp[0][0])
        return "perfect";

    for(int i=0; i<x; ++i){
        if(dp[i][0]){
            ostringstream oss;
            oss << "good " << (i / 2);
            if(i % 2 == 0)
                oss << ".000";
            else
                oss << ".500";
            return oss.str();
        }
    }

    return "try again";
}

int main()
{
    int c;
    cin >> c;

    while(--c >= 0){
        cin >> n;
        a.resize(n);
        for(int i=0; i<n; ++i)
            cin >> a[i];
        sort(a.begin(), a.end());

        int q;
        cin >> q;
        while(--q >= 0){
            int x, v;
            cin >> x >> v;
            cout << solve(x, v) << endl;
        }

        if(c > 0)
            cout << endl;
    }

    return 0;
}