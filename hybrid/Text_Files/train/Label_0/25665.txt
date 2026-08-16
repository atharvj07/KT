#include<bits/stdc++.h>
using namespace std;

//======================
//
// Template OleschY
//
// Die M�glichkeiten der deutschen Grammatik k�nnen
// einen, wenn man sich darauf, was man ruhig, wenn
// man m�chte, sollte, einl�sst, �berraschen.
// - @Gedankenbalsam
//
//======================

//======================
//      Output/Debug
//======================

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& v)
{
    os << "[";
    for (int i = 0; i < v.size(); ++i)
    {
        os << v[i];
        if (i != v.size() - 1)
            os << ", ";
    }
    os << "]\n";
    return os;
}

template <typename T, typename U>
ostream& operator<<(ostream& os, const pair<T, U>& p)
{
    os << "[";
    os << p.first;
    os << ", ";
    os << p.second;
    os << "]";
    return os;
}

#ifndef ONLINE_JUDGE
#define debug(x) cout << (#x) << " is " << (x) << endl
#else
#define debug(...) 42
#endif

//======================
// Solution Single testcase
//======================

int n, m;

struct _rob
{
    int id;
    int pos;
    bool right = false;
    int boom = -1;
    bool operator<(const _rob& other) const
    {
        return pos < other.pos;
    }
    bool evenpos()
    {
        return (pos % 2) == 0;
    }
    void mirror()
    {
        if(right)
        {
            pos = m + (m - pos);
        }
        else
        {
            pos = 0 + (0 - pos);
        }
        right = !right;
    }
};


int solve()
{
    vector<_rob> robs;
    cin >> n >> m;
    robs.resize(n);
    for(int i = 0; i < n; ++i)
    {
        cin >> robs[i].pos;
        robs[i].id = i;
    }
    for(int i = 0; i < n; ++i)
    {
        char c;
        cin >> c;
        if(c == 'R')
            robs[i].right = true;
    }
    sort(robs.begin(), robs.end());

    //check for odds first
    stack<int> robid;
    for(int i=0; i<n; i++)
    {
        if(!robs[i].evenpos())
        {
            if(!robs[i].right)
            {
                if(robid.empty())
                {
                    robs[i].mirror();
                }
                else
                {
                    int time = (robs[i].pos - robs[robid.top()].pos) / 2;
                    robs[i].boom = time;
                    robs[robid.top()].boom = time;
                    robid.pop();
                }
            }
            if(robs[i].right)
            {
                robid.push(i);
            }

        }
    }
    while(!robid.empty())
    {
        int idlast = robid.top();
        robid.pop();
        robs[idlast].mirror();
        if(!robid.empty())
        {
            int second = robid.top();
            robid.pop();
            int time = (robs[idlast].pos - robs[second].pos) / 2;
            robs[idlast].boom = time;
            robs[second].boom = time;
        }
    }

    // now even
    for(int i=0; i<n; i++)
    {
        if(robs[i].evenpos())
        {
            if(!robs[i].right)
            {
                if(robid.empty())
                {
                    robs[i].mirror();
                }
                else
                {
                    int time = (robs[i].pos - robs[robid.top()].pos) / 2;
                    robs[i].boom = time;
                    robs[robid.top()].boom = time;
                    robid.pop();
                }
            }
            if(robs[i].right)
            {
                robid.push(i);
            }

        }
    }
    while(!robid.empty())
    {
        int idlast = robid.top();
        robid.pop();
        robs[idlast].mirror();
        if(!robid.empty())
        {
            int second = robid.top();
            robid.pop();
            int time = (robs[idlast].pos - robs[second].pos) / 2;
            robs[idlast].boom = time;
            robs[second].boom = time;
        }
    }


    auto comp = [](_rob const & a, _rob const & b)
    {
        return a.id < b.id;
    };
    sort(robs.begin(), robs.end(), comp);

    for(auto rob : robs)
    {
        cout << rob.boom << " ";
    }
    cout << "\n";

    return 0;
}

//======================
// Technical stuff
//======================

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    //freopen("a.out","w",stdout); // console output is better (in most cases)
#else
    // add i/o method of specific testing system
#endif
    int ntest = 1;
    cin >> ntest;
    for(int test = 0; test < ntest; ++test)
    {
        solve();
    }
    return 0;
}
