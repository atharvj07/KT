import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();
		int[][] a=new int[2][N];
		for(int i=0;i<2;i++) {
			for(int j=0;j<N;j++) {
				a[i][j]=sc.nextInt();
			}
		}
		
		int ans=0;
		int c=0;
		for(int i=0;i<N;i++) {
			c=0;
			for(int j=0;j<=i;j++) {
				c+=a[0][j];
			}
			for(int j=i;j<N;j++) {
				c+=a[1][j];
			}
			if(ans<c)ans=c;
		}
		System.out.println(ans);

		}
	}
