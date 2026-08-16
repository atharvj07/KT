import java.util.Scanner;

class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int A[] = new int[n];
		int i, j, key;
		for(i=0; i<n; i++){
			A[i] = sc.nextInt();
		}
		print(A);
		for(i=1; i<n; i++){
			key = A[i];
			j = i - 1;
			while(j>=0 && A[j]>key){
				A[j+1] = A[j];
				j--;
			}
			A[j+1] = key;
			print(A);
		}
	}
	public static void print(int A[]){
		for(int i=0; i<A.length; i++){
			if(i!=0) System.out.print(" ");
			System.out.print(A[i]);
		}
		System.out.println();
	}
}