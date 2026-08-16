#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<ll> vec;
#define logarr(x)                  \
    for (i = 0; i < x.size(); i++) \
        cout << x[i] << " ";       \
    cout << endl;
#define dbg(x) cout << #x << " = " << x << endl
#define vecIN(x)            \
    {                       \
        ll element7024;     \
        cin >> element7024; \
        x.pb(element7024);  \
    }
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define fast_cin()                    \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sortall(x) sort(all(x))
#define loop(x, n) for (ll i = x; i < n; i++)
#define PI 3.1415926535897932384626
ll i;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        int flag = 0;
        int c = 0, d = 0;
        if (is_sorted(s.begin(), s.end()))
        {
            cout << "YES" << endl;
        }
        else
        {
            int y = 0;
            for (int i = s.length() - 1; i > 0; i--)
            {
                if (s[i] == '0' && s[i - 1] == '0')
                {
                    y = i - 1;
                    flag = 1;
                    break;
                }
            }
            if (flag == 0)
            {
                cout << "YES" << endl;
                continue;
            }
            int flag2 = 0;
            for (int i = y; i > 0; i--)
            {
                if (s[i] == '1' && s[i - 1] == '1')
                {
                    flag2 = 1;
                    break;
                }
            }
            if (flag2 == 0)
            {
                cout << "YES" << endl;
            }
            else
                cout << "NO" << endl;
        }
    }
}