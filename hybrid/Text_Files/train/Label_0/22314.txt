#include<iostream>
#include<vector>
#include<algorithm>
#include<tuple>

using namespace std;

int main() {
    int n, u, v, m;
    cin >> n >> u >> v >> m;
    bool draw = true;
    int val;
    vector<pair<int,int>> usagi(1000001), neko(1000001);
    vector<int> usanum,nekonum;
    for(int i=0 ; i<n ; i++){
        for(int j=0; j<n ; j++){
            cin >> val;
            usagi[val] = pair<int,int>(i,j);
            usanum.push_back(val);
        }
    }
    for(int i=0 ; i<n ; i++){
        for(int j=0; j<n ; j++){
            cin >> val;
            neko[val] = pair<int,int>(i,j);
            nekonum.push_back(val);
        }
    }
    sort(usanum.begin(),usanum.end());
    sort(nekonum.begin(),nekonum.end());
    vector<int> usagi_dp(2*n+2,0), neko_dp(2*n+2,0);
    int hoge,fuga;
    int uwin=0,nwin=0;
    vector<bool> uc(2*n+2,false),nc(2*n+2,false);

    for(int i=0 ; i< m ;i++){
        cin >> val;
        if(binary_search(usanum.begin(), usanum.end(),val)){
            tie(hoge,fuga) = usagi[val];
            usagi_dp[hoge]++;
            if(!uc[hoge] && usagi_dp[hoge]>=n){
                uc[hoge]=true;
                uwin++;
            }
            usagi_dp[n+fuga]++;
            if(!uc[n+fuga] && usagi_dp[n+fuga]>=n){
                uc[n+fuga]=true;
                uwin++;
            }
            if(hoge==fuga){
                usagi_dp[2*n]++;
                if(!uc[2*n] && usagi_dp[2*n]>=n){
                    uc[2*n]=true;
                    uwin++;
                }
            }
            if(hoge == n-fuga -1){
                usagi_dp[2*n+1]++;
                if(!uc[2*n+1] && usagi_dp[2*n+1]>=n){
                    uc[2*n+1]=true;
                    uwin++;
                }
            }
        }
        //uwin = (usagi_dp[hoge]>=u) || (usagi_dp[n+fuga]>=u) || (usagi_dp[2*n]>=u) || (usagi_dp[2*n+1]>=u);
        if(binary_search(nekonum.begin(), nekonum.end(),val)){
            tie(hoge,fuga) = neko[val];
            neko_dp[hoge]++;
            neko_dp[n+fuga]++;
            if(!nc[hoge] && neko_dp[hoge]>=n){
                nc[hoge]=true;
                nwin++;
            }
            if(!nc[n+fuga] && neko_dp[n+fuga]>=n){
                nc[n+fuga]=true;
                nwin++;
            }
            if(hoge==fuga){
                neko_dp[2*n]++;
                if(!nc[2*n] && neko_dp[2*n]>=n){
                    nc[2*n]=true;
                    nwin++;
                }
            }
            if(hoge == n-fuga -1){
                neko_dp[2*n+1]++;
                if(!nc[2*n+1] && neko_dp[2*n+1]>=n){
                    nc[2*n+1]=true;
                    nwin++;
                }
            }
            
        }
        //nwin = (neko_dp[hoge]>=v) || (neko_dp[n+fuga]>=v) || (neko_dp[2*n]>=v) || (neko_dp[2*n+1]>=v);
        if(n==1){
            uwin = min(1,uwin);
            nwin = min(1,nwin);
        }
        if( uwin >= u ){
            if(nwin >= v)break;
            cout << "USAGI" << endl;
            draw=false;
            break;
        }else if(nwin >= v){
            cout << "NEKO" << endl;
            draw=false;
            break;
        }
    }
    if(draw) cout << "DRAW" << endl;
    return 0;
}

