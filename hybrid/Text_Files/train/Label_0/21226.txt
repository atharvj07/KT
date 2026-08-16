#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define int ll

inline ll toInt(string s) {ll v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> inline T sqr(T x) {return x*x;}

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define all(a)  (a).begin(),(a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define pb push_back
#define mp make_pair
#define each(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define exist(s,e) ((s).find(e)!=(s).end())
#define range(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  range(i,0,n)
#define clr(a,b) memset((a), (b) ,sizeof(a))
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

const double eps = 1e-10;
const double pi  = acos(-1.0);
const ll INF =1LL << 62;
const int inf =1 << 24;

inline ll f(ll lb, ll ub, int idx){
    lb--;

    return idx * ((ub - lb) - (ub / 3 - lb / 3) - (ub / 5 - lb / 5) + (ub / 15 - lb / 15)) + 4 * ((ub / 3 - lb / 3) + (ub / 5 - lb / 5));
}

signed main(void){
    for(ll s; cin >> s;){
        ll len = 0;
        int idx;
        ll lb, ub;
        ll min_val = 0;

        range(i, 1, 18){
            lb = min_val;
            ub = pow(10, i) - 1;

            if(s - f(lb + 1, ub, i) > len) len += f(lb + 1, ub, i);
            else{
                idx = i;
                break;
            }

            min_val = ub;
        }

        lb = min_val + 1, ub = lb * 10 - 1;
        ll mid, len_cur;


        while(lb < ub){
            mid = (lb + ub) / 2;

            len_cur = len + f(min_val + 1, mid, idx);

            if(len_cur < s) lb = mid + 1;
            else if(len_cur > s) ub = mid - 1;
            else lb = mid, ub = mid;
        }

        ll t = lb;
        len_cur = len + f(min_val + 1, lb, idx);

        if(!(lb % 3)) len_cur -= 4;
        if(!(lb % 5)) len_cur -= 4;
        if(lb % 3 && lb % 5) len_cur -= idx;

        ll w = s - len_cur;

        ll cur = lb;

        string res;

        while(res.size() <= 20 + w){
            if(cur % 3 == 0) res += "Fizz";
            if(cur % 5 == 0) res += "Buzz";
            if(cur % 3 && cur % 5) res += toString(cur);

            cur++;
        }
        rep(i, 20){
            cout << res[i + w - 1];
        }
        cout << endl;
    }

	return 0;
}