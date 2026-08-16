#include<bits/stdc++.h>
#define Rint register int
using namespace std;
const int N = 1000003;
int n, a[N], ans;
bool f;
int main(){
    scanf("%d", &n);
    for(Rint i = 0;i < n;++ i){
        scanf("%1d", a + i); -- a[i]; f |= a[i] == 1;
    }
    if(!f) for(Rint i = 0;i < n;++ i) a[i] >>= 1;
    for(Rint i = 0;i < n;++ i) if(!(i & n - 1 - i)) ans ^= a[i] & 1;
    if(!f) ans <<= 1;
    printf("%d", ans);
}