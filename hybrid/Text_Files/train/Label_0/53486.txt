import java.util.*;
import java.math.*;
import java.io.*;
public class Main {
	static HashMap<String,String> map = new HashMap<String,String>();
	static ArrayList<String> list = new ArrayList<String>();

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] c = new int[n];
		int[] g = new int[n];
		for(int i = 0; i < n; i++) {
			c[i] = sc.nextInt();
			g[i] = sc.nextInt();
		}
		Data[] data = new Data[n];
		for(int i = 0; i < n; i++) {
			data[i] = new Data(c[i],g[i]);
		}
		Arrays.sort(data);
		int[][] gSum = new int[10][n];
		int id = 1;
		for(int i = 0; i < n; i++) {
			if(i != 0 && data[i].g != data[i-1].g) {
				id = 1;
			}
			gSum[data[i].g-1][id] = gSum[data[i].g-1][id-1] + data[i].c;
			id++;
		}
		
		
		
		int[][] dp = new int[11][k+1];
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < k+1; j++) {
				for(int kk = 0; kk < n; kk++) {
					if(kk + j > k) break;
					if(kk != 0 && gSum[i][kk] == 0) break;
					dp[i+1][j + kk] = Math.max(gSum[i][kk] + dp[i][j] + (kk)*(kk-1),dp[i+1][j+kk]);
				}
			}
		}
		
		
		
		int max = dp[10][k];
		
		System.out.println(max);
		
		
		
		
		
		
		
		
		
		
		
		
	}
	
	static class Data implements Comparable<Data> {
		int c;
		int g;
		Data(int a, int b) {
			c = a;
			g = b;
		}
		@Override
		public int compareTo(Data o) {
			if(this.g == o.g) return o.c - this.c;
			return this.g - o.g;
		}
	}

}