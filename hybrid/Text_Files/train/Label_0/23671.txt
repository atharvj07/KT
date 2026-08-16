#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define  pb  push_back
int main(){
    int tmp;
    int n;cin>>n;
    vector<int> a;
    vector<int> b;
    vector<int> c;
    int a_n;cin>>a_n;for(int i = 0; a_n > i; i++)cin>>tmp,a.pb(tmp);sort(a.begin(),a.end());
    int b_n;cin>>b_n;for(int i = 0; b_n > i; i++)cin>>tmp,b.pb(tmp);sort(b.begin(),b.end());
    int c_n;cin>>c_n;for(int i = 0; c_n > i; i++)cin>>tmp,c.pb(tmp);sort(c.begin(),c.end());
    int nwa = 0;
    int nwb = 0;
    int nwc = 0;
    bool bla,blb,blc;
    int ans = 0;
    for(int i = 1; n >= i; i++){
        bla = false;
        blb = false;
        blc = false;
        if(!a.empty()&&a[nwa]==i){
            bla = true;
            nwa++;
        }
        if(!b.empty()&&b[nwb]==i){
            blb = true;
            nwb++;
        }
        if(!c.empty()&&c[nwc]==i){
            blc = true;
            nwc++;
        }
        //cout << (bla?"a":"b") << " " << (blb?"a":"b") << " " << (blc?"a":"b") << endl;
        if((!bla && blc) || (blb && blc))ans++;
    }
    cout << ans << endl;
    
}

