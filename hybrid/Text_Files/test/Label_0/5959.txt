#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
#include<map>
using namespace std;

int gcd(int a,int b) {
    if(a<b)return gcd(b,a);
    else if(b==0)return a;
    else return gcd(b,a%b);
}

int main() {
    int N,K;
    cin >> N >> K;
    vector<pair<short,short>> P(N);
    int i,j;
    for(i=0;i<N;i++)cin >> P[i].first >> P[i].second;
    sort(P.begin(),P.end());
    bool f = true;
    for(i=0;i<N-1;i++) {
        vector<double> list(1,100000);
        for(j=i+1;j<N;j++)list.push_back(P[i].first==P[j].first?20000:(double)(P[i].second-P[j].second)/(P[i].first-P[j].first));
        sort(list.begin(),list.end());
        int cnt = 1;
        for(j=1;j<list.size();j++) {
            if(list[j-1]==list[j])cnt++;
            else {
                if(cnt>=K-1)f = false;
                cnt = 1;
            }
        }
    }
    cout << (f?0:1) << endl;
}
