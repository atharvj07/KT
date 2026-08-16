import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static int[][] dp;
	static char[] in1, in2;
	final static int BIG_PRIME = 1000000007;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
		
		in1 = br.readLine().toCharArray();
		in2 = br.readLine().toCharArray();
		
		dp = new int[in1.length][in2.length];
		for(int[] i : dp){
		    Arrays.fill(i, -1);
		}
		  
		System.out.println(search(0, 0) % BIG_PRIME);
	}
	static int search(int i, int j){
		  int count = 0;
		  
		  if(j == in2.length)return 1;
		  if(i == in1.length)return 0;
		  
		  if(dp[i][j] != -1){
		    return dp[i][j];
		  } else if(in1[i] == in2[j]){
		    count = search(i + 1, j + 1)% BIG_PRIME + search(i + 1, j)% BIG_PRIME;
		  } else {
		    count = search(i + 1, j)% BIG_PRIME;
		  }
		  
		  return dp[i][j] = count;
		}
}

