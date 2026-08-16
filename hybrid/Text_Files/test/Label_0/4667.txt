#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int MAXN = 100100;

int N;
ll s[MAXN];

int main()
{
    ios_base::sync_with_stdio(0);
    
    cin >> N;
    for (int i = 0; i < N; i++)
        cin >> s[i];

    ll ans = 0;
    for (int i = 1; i < N; i++)
    {
        ll res = 0;
        for (int j = 0; j + i < N; j += i)
        {
            if ((N - 1) % i == 0 && 2 * j >= (N - 1))
                break;
            res += s[j];
            res += s[N-1-j];
            ans = max (ans, res);
        }
    }
    cout << ans << "\n";
}