import java.io.*;
import java.math.BigDecimal;
import java.util.*;

public class Main {
	static int INF = 2 << 27;
	static int[] vx = {1,0,-1,0};
	static int[] vy = {0,1,0,-1};
	public static void main(String[] args) {	
		//FastScanner sc = new FastScanner();
		Scanner sc = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		int N = sc.nextInt();
		int m = sc.nextInt();
		int[] c = new int[m];
		int[] d = new int[m];
		boolean[] triple = new boolean[N+1];
		for(int i = 0; i < m; i++) {
			c[i] = sc.nextInt();
			d[i] = sc.nextInt();
			for(int j = c[i]; j < d[i]; j++) {
				triple[j] = true;
			}
		}
		int sum = 0;
		for(int i = 0; i <= N; i++) {
			if(triple[i]) sum += 3;
			else sum += 1;
		}
		System.out.println(sum);
		
		
		
		
		
	}
}