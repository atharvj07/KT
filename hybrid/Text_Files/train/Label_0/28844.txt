#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<ll, ld> pairID;
#define FOR(i,n) for(int i=0; i<int(n); i++)
#define FOR1(i,m,n) for(int i=int(m); i<int(n); i++)

ll N, L;
deque<pairID> A;

int main(int argc, char *argv[])
{
    ll t, v;
    ld total_heat;

    scanf("%lld%lld", &N, &L);
    scanf("%lld%lld", &t, &v);
    
    A.push_front(make_pair(v, t));
    total_heat = (ld)v * t;
    printf("%.7f\n", (double)total_heat / L);
    
    FOR1(i,1,N) {
        pairID back;
        ll vol;

        scanf("%lld%lld", &t, &v);
        total_heat += (ld)v * t;
        
        vol = v;
        while (vol > 0) {
            back = A.back();
            A.pop_back();
            vol -= back.first;
            total_heat -= back.first * back.second;
        }
        if (vol != 0) {
            A.push_back(make_pair(-vol, back.second));
            total_heat += -vol * back.second;
        }

        ld heat = v * t;
        vol = v;
        while(A.size() > 0 && heat / vol <= A.front().second) {
            heat += A.front().first * A.front().second;
            vol += A.front().first;
            A.pop_front();
        }
        A.push_front(make_pair(vol, heat / vol));

        printf("%.7f\n", (double)total_heat / L);
    }
    return 0;
}
