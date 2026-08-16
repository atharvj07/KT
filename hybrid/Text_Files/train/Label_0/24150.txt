/*
        SUPTO
        UNIVERSITY OF DHAKA
*/
#include <bits/stdc++.h>
using namespace std;
#define D(x) cerr<<#x " = "<<(x)<<endl
#define pb push_back
#define ff first
#define ss second
#define mem(a) memset(a,0,sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
typedef long long int ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define MAX 100005
#define MAXL 20
#define MAXE 100000
//const int mod = 1000000007;
//const int inf = 1<<30;
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};
//const double eps=1e-9;
const double pi=acos(-1.0);
int dblcmp(ll d) {
    if(d == 0) return 0;
    return d>0?1:-1;
}
inline ll sqr(ll x){return x*x;}
struct point  {
    ll x,y;
    point(){}
    point(ll _x,ll _y): x(_x),y(_y){};
    bool operator==(point a)const { return dblcmp(a.x-x)==0&&dblcmp(a.y-y)==0; }
    bool operator<(point a)const { return dblcmp(a.x-x)==0?dblcmp(y-a.y)<0:x<a.x; }
    double len() { return hypot(x,y); }
    double len2() { return x*x+y*y; }
    double distance(point p) { return hypot(x-p.x,y-p.y); }
    point add(point p) { return point(x+p.x,y+p.y); }
    point sub(point p) { return point(x-p.x,y-p.y); }
    point mul(double b) { return point(x*b,y*b); }
    point div(double b) { return point(x/b,y/b); }
    ll dot(point p) { return x*p.x+y*p.y; }
    ll det(point p) { return x*p.y-y*p.x; }
} ar[MAX], upper[MAX], lower[MAX];
ll total1[MAX], total2[MAX];

int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("codes.out", "w", stdout);
    int n, i;
    scanf("%d", &n);
    for(i = 0; i < n; i++) scanf("%lld %lld", &ar[i].x, &ar[i].y);
    sort(ar, ar+n);
    int topu = 0, topl = 0;
    upper[0] = lower[0] = ar[0];
    total1[0] = 0;
    ll area1 = 0, area2 = 0;
    for(i = 1; i < n; i++)
    {
        while(topu && upper[topu].sub(ar[i]).det(upper[topu-1].sub(ar[i])) <= 0)
        {
            area1 -= upper[topu-1].det(upper[topu]);
            topu--;
        }
        while(topl && lower[topl].sub(ar[i]).det(lower[topl-1].sub(ar[i])) >= 0)
        {
            area2 += lower[topl-1].det(lower[topl]);
            topl--;
        }
        upper[++topu] = ar[i];
        lower[++topl] = ar[i];
        if(topu) area1 += upper[topu-1].det(upper[topu]);
        if(topl) area2 -= lower[topl-1].det(lower[topl]);
        total1[i] = abs(area1+area2);
    }
    topu = topl = 0;
    upper[0] = lower[0] = ar[n-1];
    total2[n] = total2[n-1] = 0;
    area1 = area2 = 0;
    for(i = n-2; i >= 0; i--)
    {
        while(topu && upper[topu].sub(ar[i]).det(upper[topu-1].sub(ar[i])) <= 0)
        {
            area1 -= upper[topu-1].det(upper[topu]);
            topu--;
        }
        while(topl && lower[topl].sub(ar[i]).det(lower[topl-1].sub(ar[i])) >= 0)
        {
            area2 += lower[topl-1].det(lower[topl]);
            topl--;
        }
        upper[++topu] = ar[i];
        lower[++topl] = ar[i];
        if(topu) area1 += upper[topu-1].det(upper[topu]);
        if(topl) area2 -= lower[topl-1].det(lower[topl]);
        total2[i] = abs(area1+area2);
    }
    ll ans = total1[n-1];
    for(i = 0; i < n; i++)
    {
        if(i < n-1 && ar[i].x != ar[i+1].x) ans = min(ans, total1[i]+total2[i+1]);
    }
    printf("%lld\n", (ans+1)/2);
    return 0;
}