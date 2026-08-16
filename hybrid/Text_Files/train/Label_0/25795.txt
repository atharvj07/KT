#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    vector<int> ans(0);
    for(;;){
        int n,l,r; cin >> n >> l >> r;
        if (n == 0 && l == 0 && r == 0) break;
        int a[n+1];
        fill(a,a+n+1,0);
        for(int i = 1; i < n+1; i++){
            cin >> a[i];
        }
        bool flg;
        int cnt = 0;
        for(int i = l; i <= r; i++){
            int x = i;
            flg = false;
            for(int num = 1; num < n+1; num++){
                if (x % a[num] == 0){
                    flg = true;
                    if (num % 2 == 1){
                        cnt++;
                        break;
                    }
                }
                if(flg) break;
            }
            if (!flg){
                if (n % 2 == 0) cnt++;
            }
        }
        ans.push_back(cnt);
    }
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << endl;
    }
}
