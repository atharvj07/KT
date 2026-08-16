#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n;
    cin >> n;

    vector<int> a(n);
    for(int i = 0 ; i < n ; ++i){
        cin >> a[i];
        for(int j = 0 ; j < i ; ++j){
            if(abs(a[i] - a[j]) % (n - 1) == 0){
                cout << a[i] << " " << a[j] << endl;
                return 0;
            }
        }
    }

    return 0;
}
