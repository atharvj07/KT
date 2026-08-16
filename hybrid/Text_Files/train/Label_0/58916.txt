import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	
	private static final Scanner IN = new Scanner(System.in);
	
	private static final int INFINITE = Integer.MAX_VALUE >> 4;
	private static final int MAX_N = 100;
	
	private final int[] distance = new int[MAX_N];
	private final int[][] previous  = new int[MAX_N][MAX_N];
	private final int[] previousN = new int[MAX_N];
	private final PriorityQueue<Long> que = new PriorityQueue<Long>(MAX_N * MAX_N);
	
	private void dijkstra() {
		
		Arrays.fill(distance, 0, n, INFINITE);
		for (int i = 0; i < n; i ++) {
			
			Arrays.fill(previous[i], 0, n, - 1);
		}
		Arrays.fill(previousN, 0, n, 0);
		distance[t] = 0;
		que.add((long) distance[t] << Integer.SIZE | t);
		
		while (!que.isEmpty()) {
			
			long d_v = que.remove();
			int  v = (int) d_v;
			if (distance[v] < d_v >> Integer.SIZE) {
				
				continue;
			}
			
			for (int i = 0; i < n; i ++) {
				
				int newD = distance[v] + a[v][i];
				if (distance[i] > newD) {
					
					distance[i] = newD;
					previousN[i] = 0;
					previous[i][previousN[i] ++] = v;
					que.add((long) distance[i] << Integer.SIZE | i);
					
				} else if (distance[i] == newD) {
					
					previous[i][previousN[i] ++] = v;
				}
			}
		}
	}
	
	private double[][] augmented = new double[MAX_N][MAX_N + 1];
	
	private void gaussJordan() {
		
		for (int i = 0; i < n; i ++) {
			
			int pivot = i;
			for (int j = i + 1; j < n; j ++) {
				
				if (Math.abs(augmented[j][i]) > Math.abs(augmented[pivot][i])) {
					
					pivot = j;
				}
			}
			double[] tmp = augmented[i];
			augmented[i]     = augmented[pivot];
			augmented[pivot] = tmp;
			
			for (int j = i + 1; j <= n; j ++) {
				
				augmented[i][j] /= augmented[i][i];
			}
			
			for (int j = 0; j < n; j ++) {
				
				if (i != j) {
					
					for (int k = i + 1; k <= n; k ++) {
						
						augmented[j][k] -= augmented[j][i] * augmented[i][k];
					}
				}
			}
		}
	}
	
	private int n;
	private int s;
	private int t;
	private final int[] q = new int[MAX_N];
	private final int[][] a = new int[MAX_N][MAX_N];
	private final int[] edgeN = new int[MAX_N];
	
	private void run() {
		
		while(((n = IN.nextInt()) | (s = IN.nextInt()) | (t = IN.nextInt())) != 0) {
			
			s --; t --;
			Arrays.fill(edgeN, 0);
			for (int i = 0; i < n; i ++) {
				
				Arrays.fill(augmented[i], 0);
				q[i] = IN.nextInt();
			}
			
			for (int i = 0; i < n; i ++) {
				
				for (int j = 0; j < n; j ++) {
					
					a[i][j] = IN.nextInt();
					
					if (a[i][j] == 0) {
						
						a[i][j] = INFINITE;
						
					} else if (q[i] == 0) {
						
						edgeN[i] ++;
					}
				}
			}
			
			dijkstra();
			
			if (distance[s] >= INFINITE) {
				
				System.out.println("impossible");
			}
			
			for (int i = 0; i < n; i ++) {
				
				if (i == t || distance[i] >= INFINITE) {
					
					augmented[i][i] = 1;
					continue;
				}
				
				if (q[i] == 0) {
					
					for (int j = 0; j < n; j ++) {
						
						if (a[i][j] >= INFINITE) {
							
							continue;
						}
						
						augmented[i][j] = - 1;
						augmented[i][n] += a[i][j];
					}
					augmented[i][i] = edgeN[i];
					
				} else {
					
					for (int j = 0; j < previousN[i]; j ++) {
						
						augmented[i][previous[i][j]] = - 1;
						augmented[i][n] += a[i][previous[i][j]];
					}
					augmented[i][i] = previousN[i];
				}
			}
			
			gaussJordan();
			
			System.out.println(augmented[s][n]);
		}
	}
	
	public static void main(String[] args) {
		
		new Main().run();
	}
}