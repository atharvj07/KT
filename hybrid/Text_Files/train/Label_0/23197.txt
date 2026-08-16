#include <bits/stdc++.h>
 
using namespace std;
typedef long long ll;

int N;
ll nt;
vector <pair <ll, ll> > res;

ll gcd (ll a, ll b)
{
    if (b == 0) return a;
    return gcd (b, a % b);
}

int main()
{
    ios_base::sync_with_stdio(0);

    cin >> N;
    nt = 0;
    for (int i = 0; i < N; i++)
    {
        int a, b;
        cin >> a >> b;
        if (a < b)
        {
            nt += b - a;
            res.push_back (make_pair (b, b));
        }
        else
        {
            res.push_back (make_pair (a, b));
        }
    }

    sort (res.begin(), res.end());

    ll shi = 0;
    ll nwhole = 0;
    ll nbest = 1, dbest = 1;
    for (int i = 0; i < N; i++)
    {

        //cout << i << " " << nt << " " << res[i].first << " " << res[i].second << endl;
        if (res[i].first <= nt)
        {
            nt -= res[i].first;
            shi = max (shi, res[i].second);
            nwhole++;
            continue;
        }
        else
        {
            // (i * res[i] + nt) / N * res[i]
            ll nnum = res[i].first - nt;
            ll dnum = max (shi, res[i].second);
            ll g = gcd (nnum, dnum);
            nnum /= g;
            dnum /= g;

            if (nnum * dbest < dnum * nbest)
            {
                nbest = nnum;
                dbest = dnum;
            }
            //cout << nnum / g << " " << dnum / g << "\n";
            //return 0;
        }
    }

    // (nwhole + 1 - nbest/dbest) / N
    ll tnum = (nwhole + 1) * dbest - nbest;
    ll tden = N * dbest;
    ll g = gcd (tnum, tden);
    tnum /= g;
    tden /= g;

    cout << tnum << " " << tden << "\n";
    return 0;
}