import java.io.IOException;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			final int max =sc.nextInt();
			
			if(max == 0){
				break;
			}
			
			final int n = sc.nextInt();
			final int size = n + 2;
			
			int[] map = new int[size];
			for(int i = 1; i <= n; i++){
				map[i] = sc.nextInt();
			}
			
			//int[][] adj = new int[size][max];
			boolean[][] adj = new boolean[size][size];
			for(int i = 0; i < size; i++){
				for(int j = 0; j < max; j++){
					if(i == size - 1){
						adj[i][i] = true;
						continue;
					}
					final int num = j + 1;
					final int to = Math.min(size - 1, Math.max(0, i + num));
					final int dist = Math.min(size - 1, Math.max(0, to + map[to]));
					
					adj[i][dist] = true;
				}
			}
			
			for(int k = 0; k < size; k++){
				for(int i = 0; i < size; i++){
					for(int j = 0; j < size; j++){
						adj[i][j] = adj[i][j] || (adj[i][k] && adj[k][j]);
					}
				}
			}
			
			boolean flag = true;
			for(int i = 0; i < size; i++){
				//System.out.print(i + " ");
				//System.out.print(adj[0][i] + " ");
				//System.out.println(adj[i][size-1]);
				
				if(adj[0][i] && !adj[i][size-1]){
					System.out.println("NG");
					flag = false;
					break;
				}
			}
			
			if(flag){
				System.out.println("OK");
			}
		}
	}

}