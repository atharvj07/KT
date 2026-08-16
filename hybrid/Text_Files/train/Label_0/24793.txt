#include <iostream>
using namespace std;

int main(){
	int N;
	int A[100];

	cin >> N;

	for(int i=0; i<N; i++)
		cin >> A[i];


	int count = 0;
	for(int i=0; i<N; i++){
		for(int i=1; i<N; i++){
			if(A[i-1]>A[i]){
				swap(A[i-1], A[i]);
				count++;
			}
		}
	}

	for(int i=0; i<N; i++){
		cout << A[i] << (i==N-1? "\n": " ");
	}

	cout << count << endl;

	return 0;
}
