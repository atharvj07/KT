#include<bits/stdc++.h>
using namespace std;
const long long int INF = 1000000000000000000;
int main(){
    int N, K;
    cin >> N >> K;
    long long int a[N];
    for (int i = 0; i < N; i++)
    {
        cin >> a[i];
    }


    long long int ans = INF;
    for (int bit = 0; bit < (1 << N); bit++)
    {
        int v = 0;
        long long int t = 0;
        long long int sum = 0;
        for (int i = 0; i < N; i++)
        {
            if(t < a[i]){
                t = a[i];
                v++;
            }
            else if(bit & (1 << i)){
                sum += t - a[i] + 1;
                v++;
                t++;
            }
        }
        if(v >= K) ans = min(ans, sum);
    }
    cout << ans << endl;
}