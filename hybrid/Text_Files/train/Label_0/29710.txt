#include<iostream>
using namespace std;

int main() {
    int n, c[10001]={};
    cin >> n;
    int a[n],b[n];
    for (int i=0; i<n; i++) {
        cin >> a[i];
        c[a[i]]++;
    }
    for (int i=1; i<10001; i++) {
        c[i] = c[i] + c[i-1];
    }
    for (int i=0; i<n ; i++) {
        b[c[a[i]]] = a[i];
        c[a[i]]--;
    }
    for (int i=1; i<n; i++) {
        cout << b[i] << " ";
    }
    cout << b[n] << endl;
}
