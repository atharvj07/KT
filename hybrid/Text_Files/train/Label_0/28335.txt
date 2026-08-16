#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) REP(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define MSG(a) cout << #a << " " << a << endl;
#define REP(i, x, n) for (int i = x; i < n; i++)
#define OP(m) cout << m << endl
typedef long long ll;
typedef unsigned long long ull;

int main()
{
    map<string, vector<int>> mp;

    string s;
    int n;
    while (cin >> s >> n)
    {
        mp[s].push_back(n);
    }

    for (auto a : mp)
    {
        OP(a.first);
        sort(ALL(a.second));
        rep(i, a.second.size())
        {
            i != a.second.size() - 1 ? cout << a.second[i] << " " : OP(a.second[i]);
        }
    }

    return 0;
}
