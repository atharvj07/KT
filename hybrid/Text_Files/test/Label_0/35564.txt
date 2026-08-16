import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
	
	int N;
	int[] A;
	Map<Integer, Integer> nums ;
	int[][] memo;
	
	public void run() throws Exception{
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(reader.readLine());
		
		StringTokenizer tok = new StringTokenizer(reader.readLine());
		nums = new HashMap<>(N * 2);
		
		memo = new int[N][N];
		for(int i = 0; i < N; i++) {
			for(int j= 0; j< N; j++) {
				memo[i][j] = -1;
			}
		}
		
		A = new int[N];
		for(int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(tok.nextToken());
		}
		
		Arrays.sort(A);
		
		for(int i = 0; i < N; i++) {
			nums.put(A[i], i);
		}
		int answer = 0;
		for(int i = 0; i < N; i++) {
			for(int j = i + 1; j < N; j++) {
				answer = Math.max(answer, dfs(i, j) + 2);
			}
		}
		System.out.println(answer);
	}
	
	public int dfs(int i, int j) {
		if(memo[i][j] != -1) return memo[i][j];
		
		int diff = A[j] - A[i];
		Integer ni = nums.get(A[j] + diff);
		if(ni == null) {
			return memo[i][j] = 0;
		}else {
			return memo[i][j] = dfs(j, ni) + 1;
		}
	}
	
	
	public static void main(String[] args) throws Exception{
		new Main().run();
	}
}

