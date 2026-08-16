import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static final int MAX_NODES = 51 * 51;
	
	public static final boolean[][] mul(boolean[][] one, boolean[][] two, final int NODES){
		boolean[][] ret = new boolean[NODES][NODES];
		
		for(int h = 0; h < NODES; h++){
			for(int v = 0; v < NODES; v++){
				if(ret[h][v]){
					continue;
				}
				
				for(int t = 0; t < NODES; t++){
					ret[h][v] = one[h][t] && two[t][v];
					
					if(ret[h][v]){
						break;
					}
				}
			}
		}
		
		return ret;
	}
	
	public static final boolean[][] pow(boolean[][] adj, final int NODES, final int Z){
		if(Z == 1){
			return adj;
		}else if(Z % 2 == 0){
			boolean[][] ret = pow(adj, NODES, Z / 2);
			return mul(ret, ret, NODES);
		}else{
			return mul(adj, pow(adj, NODES, Z - 1), NODES);
		}
	}

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			final int N = sc.nextInt();
			final int M = sc.nextInt();
			final int Z = sc.nextInt();
			
			if(N == 0 && M == 0 && Z == 0){
				break;
			}
			
			int[] pre = new int[2 * M];
			int[] now = new int[2 * M];
			
			for(int i = 0; i < M; i++){
				int s = sc.nextInt();
				int t = sc.nextInt();
				
				pre[i * 2] = s;
				now[i * 2] = t;
				pre[i * 2 + 1] = t;
				now[i * 2 + 1] = s;
			}
			
			boolean[][] A = new boolean[2 * M + 1][2 * M + 1];
			for(int i = 0; i < 2 * M; i++){
				for(int j = 0; j < 2 * M; j++){
					if(now[i] == pre[j] && now[j] != pre[i]){
						A[i][j] = true;
					}
				}
			}
			
			for(int i = 0; i < 2 * M; i++){
				if(pre[i] == 1){
					A[2 * M][i] = true;
				}
			}
			
			A = pow(A, 2 * M + 1, Z);
			
			boolean flag = false;
			for(int i = 0; i < 2 * M; i++){
				if(now[i] == N && A[2 * M][i]){
					flag = true;
					break;
				}
			}
			
			System.out.println(flag ? "yes" : "no");
		}
	}

}