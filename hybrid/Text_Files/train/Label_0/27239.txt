#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <utility>
#include <queue>
#include <set>
#include <map>
#include <iomanip>
#include <cstdio>

using namespace std;
typedef  long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
#define  MP make_pair
#define  PB push_back
#define inf  1000000007
#define rep(i,n) for(int i=0;i<(int)(n);++i)
template<typename A, size_t N, typename T>
void Fill(A (&array)[N], const T &val){
    std::fill( (T*)array, (T*)(array+N), val );
}
int main(){
    int a,b,s,k;
    cin >> a >> b >> k;
    s = b-a;
    vector<ll>t(k+1);
    rep(i,k+1){
        cin >> t[i];
    }
    ll dp[1010][32]={};
    Fill(dp,(ll)10000000000);
    ll X[1010]={};
    Fill(X,(ll)10000000000);
    X[0] = 0;
    X[1] = 0;
    X[2] = t[0]+t[1];
    dp[2][1] = t[0]+t[1];
    for(int i=3;i<=s;i++){
        for(int j=1;j<min(i,k+1);j++){
            if(j==1){
                for(int p=1;p<i;p++){
                    dp[i][j] = min(dp[i][j],X[p]+p*t[0]+X[i-p]+(i-p)*t[1]);
                }
            }else{
                for(int p=1;p<=i-j;p++){
                    dp[i][j] = min(dp[i][j],dp[i-p][j-1]+X[p]+p*t[j]);
                }
            }
            X[i] = min(X[i],dp[i][j]);
        }
    }
    cout << fixed << setprecision(10) <<  (double)X[s]/(double)s << endl;
    return 0;
}
