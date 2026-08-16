import java.util.*;
import java.io.*;

public class Main{
	public static int solve(int[] n){
		if( n.length == 1 ){
			return n[0]%10;
		}
		int[] temp = new int[n.length-1];
		for(int i = 0; i < temp.length; i++){
			temp[i] = n[i]+n[i+1];
		}
		return solve(temp);
	}
	
	public static void main(String[] args) throws IOException{
		Scanner stdIn = null;
		List<Integer> result = new ArrayList<Integer>();
		
		try{
			stdIn = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
			while( stdIn.hasNext() ){
				long x = stdIn.nextLong();
				int[] n = new int[10];
				for(int i = 9; i >= 0; i--){
					n[i] = (int)(x%10);
					x /= 10;
				}
				result.add(solve(n));
			}
			for(Integer ans : result){
				System.out.println(ans);
			}
		} finally {
			if( stdIn != null ){
				stdIn.close();
			}
		}
	}
}