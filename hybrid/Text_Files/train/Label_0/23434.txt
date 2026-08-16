#include <bits/stdc++.h>
#define int long long
#define endl '\n'

using namespace std;

void solve()
{
    int n; cin >> n;

    vector<int> a(n);vector<int> ans(n);

    for(int i=0;i<n;++i) cin >> a[i];

    vector<int> mask(31,0);

    for(int j=0;j<31;++j) if((a[0]>>j)&1) mask[j] = 1;

    ans[0] = 0;

    for(int i = 1;i <n;++i){

        vector<int> cur(31,0);

        for(int j=0;j<31;++j) if((a[i]>>j)&1) cur[j] = 1;

        int req = 0;

        for(int j =0;j<31;++j) mask[j]=mask[j] | cur[j];

        for(int j=0;j<31;++j) if(mask[j]) req += (1<<j);

        int val = a[i] ^ req;

        ans[i] = val;

    }

    for(int i=0;i<n;++i) cout << ans[i] << " ";

    cout << endl;
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int T = 1;cin >> T;

    for (int test_case = 1; test_case <= T; test_case++)
    {
        solve();
    }
}