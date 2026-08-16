#include<bits/stdc++.h>
#define ll long long

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while(t--){
        int n,m;
        cin >> n >> m;
        vector<vector<char>> f(n, vector<char>(m));
        int count = 0;
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                cin >> f[i][j];
                if(f[i][j] == '.'){
                    count++;
                }
            }
        }
        int k = 0;
        if(count == n*m){
            for(int i = 0; i < n; ++i){
                for(int j = 0; j < m; ++j){
                    if(i == 0 && j == 0){
                        f[i][j] = 'R';
                    }else if(i-1 >= 0){
                        if(f[i-1][j] == 'R'){
                            f[i][j] = 'W';
                        }else{
                            f[i][j] = 'R';
                        }
                    }else if(j-1 >= 0){
                        if(f[i][j-1] == 'R'){
                            f[i][j] = 'W';
                        }else{
                            f[i][j] = 'R';
                        }
                    }
                }
            }
        }else{
        for(int z = 0; z < 100; ++z){
            for(int i = 0; i < n; ++i){
                for(int j = 0; j < m; ++j){
                    if(i-1 >= 0){
                        if(f[i-1][j] == 'R'){
                            f[i][j] = 'W';
                        }else if(f[i-1][j] == 'W'){
                            f[i][j] = 'R';
                        }
                    }
                    if(j-1 >= 0){
                        if(f[i][j-1] == 'R'){
                            if(f[i][j] == 'R'){
                                k = 1;
                            }
                            f[i][j] = 'W';
                        }else if(f[i][j-1] == 'W'){
                            if(f[i][j] == 'W'){
                                k = 1;
                            }
                            f[i][j] = 'R';
                        }
                    }
                    if(i+1 < n){
                        if(f[i+1][j] == 'R'){
                            if(f[i][j] == 'R'){
                                k = 1;
                            }
                            f[i][j] = 'W';
                        }else if(f[i+1][j] == 'W'){
                            if(f[i][j] == 'W'){
                                k = 1;
                            }
                            f[i][j] = 'R';
                        }
                    }
                    if(j+1 < m){
                        if(f[i][j+1] == 'R'){
                            if(f[i][j] == 'R'){
                                k = 1;
                            }
                            f[i][j] = 'W';
                        }else if(f[i][j+1] == 'W'){
                            if(f[i][j] == 'W'){
                                k = 1;
                            }
                            f[i][j] = 'R';
                        }
                    }
                }
            }
        }
        }
        if(k == 1){
            cout << "NO" << '\n';
        }else{
            cout << "YES" << '\n';
            for(int i = 0; i < n; ++i){
                for(int j = 0; j < m; ++j){
                    cout << f[i][j];
                }
                cout << '\n';
            }
        }
    }
    return 0;
}
