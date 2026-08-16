#include<bits/stdc++.h>
#define ld long double
using namespace std;

long double t[302][302][302];
bool w[302][302][302];

int n,a;

ld n2;
int tab[4];

long double dp(int a, int b, int c){
    if(a<0 || b<0 || c<0) return 0;
    if(w[a][b][c]) return t[a][b][c];
    w[a][b][c]=true;
    t[a][b][c]=(( n2+(ld)a*dp(a-1,b,c)+(ld)b*dp(a+1,b-1,c)+(ld)c*dp(a,b+1,c-1))/(ld)(a+b+c));
    return t[a][b][c];
}

int main(){

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    w[0][0][0]=true;

    cin>>n;
    n2=n;
    for(int i=0;i<n;i++) {
        cin>>a;
        tab[a]++;
    }

    cout<<setprecision(10)<<fixed<<dp(tab[1],tab[2],tab[3]);
    return 0;
}
