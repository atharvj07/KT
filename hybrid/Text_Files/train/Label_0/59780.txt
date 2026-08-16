
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt(),m=sc.nextInt(),l=sc.nextInt();
		int[][] A = new int[n][m];
		int[][] B = new int[m][l];
		long[][] C = new long[n][l];

		for(int i=0; i<n;i++) {
			for(int j=0; j<m;j++) {
				A[i][j]=sc.nextInt();
			}
		}

		for(int i=0; i<m;i++) {
			for(int j=0; j<l ;j++) {
				B[i][j]=sc.nextInt();
			}
		}

		for(int i=0; i<n; i++) {
			for(int j=0;j<l; j++) {
				long tmp=0;
				for(int k=0; k<m; k++) {
					tmp+= A[i][k]*B[k][j];
				}
				C[i][j]=tmp;
			}
		}

		for(int i=0; i<n; i++) {
			for(int j=0; j<l; j++) {
				if(j==0) {
					System.out.print(C[i][j]);
				}else {
					System.out.print(" "+C[i][j]);
				}
			}
			System.out.println("");
		}

	}
}

