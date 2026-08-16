//import java.util.Scanner;
//
//
//public class JonandOrbs {
//	
//	public static void main(String[] args) {
//		Scanner in = new Scanner(System.in);
//		int n = in.nextInt(), q = in.nextInt();
//		double t1[] = new double[n+1], t2[] = new double[n+1];
//		double probs[] = new double[100000];
//		t1[0] = 1;
//		for(int i = 0; i < 30; i++) {
//			for(int j = 0; j <= n; j++) {
//				t2[j] += t1[j] * ((double)(n - j)/(double)n);
//				if(j != 0) {
//					t1[j-1] += t2[j] * ((double)j/ (double)n);
//				}
//			}
//			double[i+1]
//		}
//		
//		for(int i = 0; i < q; i++) {
//			double qq = (in.nextDouble() - (1e-7))/2000.0;
//			int idx = 0;
//			while(memo[idx][0] < qq) {
//				idx++;
//			}
//			System.out.println(idx);
//		}
//	}
//}


 import java.util.Scanner;


public class JonandOrbs {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt(), q = in.nextInt();
		double memo[][] = new double[10000][n+1];
		memo[0][n] = 1;
		for(int i = 0; i < 10000-1; i++) {
			for(int j = 0; j <= n; j++) {
				memo[i+1][j] += memo[i][j] * ((double)(n - j)/(double)n);
				if(j != 0) {
					memo[i+1][j-1] += memo[i][j] * ((double)j/ (double)n);
				}
			}
		}
		for(int i = 0; i < q; i++) {
			double qq = (in.nextDouble() - (1e-7))/2000.0;
			int idx = 0;
			while(memo[idx][0] < qq) {
				idx++;
			}
			System.out.println(idx);
		}
	}
}