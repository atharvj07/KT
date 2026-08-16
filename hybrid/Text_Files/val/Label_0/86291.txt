#include <cstdio>

int main(){
	int A, B, AB, O;
	int n;
	char blood[2];
	A = B = AB = O = 0;
	while(scanf("%d,%s", &n, blood) != EOF){
		switch(blood[0]){
		case 'A':
			if(blood[1] == 'B'){
				AB++;
			}else {
				A++;
			}
			break;
		case 'B':
			B++;
			break;
		case 'O':
			O++;
			break;
		}
		blood[1] = 'z';
	}
	printf("%d\n%d\n%d\n%d\n", A, B, AB, O);
	return 0;
}