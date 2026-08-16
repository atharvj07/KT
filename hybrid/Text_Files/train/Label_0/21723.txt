#include<iostream>
#include<algorithm>

using namespace std;
int n,m,d[200],v[200];
int maxi[200];
int main() {
    while(1) {
        cin >> n >> m;
        if(n == 0)break;
        for(int i =0;i < n;i++)cin >> d[i] >> v[i];

        for(int i = 1;i <= m;i++)maxi[i] = 0;
        for(int i = 0;i < n;i++)maxi[d[i]] = max(maxi[d[i]],v[i]);

        int sum = 0;
        for(int i = 1;i <= m;i++)sum += maxi[i];
        cout << sum << endl;
    }
    return 0;
}
