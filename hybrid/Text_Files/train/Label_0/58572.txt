import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.TreeSet;
 
 
public class Main{
     
	public static boolean check(int pos, int[] array, int mod){
		if(pos < 2){
			return true;
		}
		
		int m = 0;
		if(pos >= 2){
			m = (array[0] + array[1] + array[2]) % mod;
		}
		
		if(pos >= 5 && ((array[3] + array[4] + array[5]) % mod != m)){
			return false;
		}
		
		if(pos >= 6 && (((array[0] + array[3] + array[6]) % mod != m) || (array[2] + array[4] + array[6]) % mod != m)){
			return false;
		}
		
		if(pos >= 7 && ((array[1] + array[4] + array[7]) % mod != m)){
			return false;
		}
		
		if(pos >= 8 && (((array[2] + array[5] + array[8]) % mod != m) || (array[0] + array[4] + array[8]) % mod != m)){
			return false;
		}
		
		return true;
	}
	
	public static int dfs(int pos, int[] array, boolean[] used, int mod){
		//System.out.println(pos);
		if(pos < 9){
			if(array[pos] != 0){
				if(used[array[pos]]){
					return 0;
				}else if(!check(pos, array, mod)){
					return 0;
				}else{
					used[array[pos]] = true;
					int ret = dfs(pos + 1, array, used, mod);
					used[array[pos]] = false;
					
					return ret;
				}
			}else{
				int sum = 0;
				
				for(int i = 1; i <= 10; i++){
					//System.out.println(Arrays.toString(used));
					if(used[i]){
						continue;
					}else{
						used[i] = true;
						array[pos] = i;
							
						if(!check(pos, array, mod)){
							array[pos] = 0;
							used[i] = false;
							continue;
						}
						sum += dfs(pos + 1, array, used, mod);
						array[pos] = 0;
						used[i] = false;
					}
				}
				
				return sum;
			}
		}else{
			return 1;
		}
	}
	
    public static void main(String[] args) throws IOException {
    	Scanner sc = new Scanner(System.in);
    	
    	while(true){
    		int[] array = new int[10];
    		
    		for(int i = 0; i < 10; i++){
    			array[i] = sc.nextInt();
    		}
    		
    		boolean flag = true;
    		for(int i = 0; i < 10; i++){
    			if(array[i] != -1){
    				flag = false;
    				break;
    			}
    		}
    		
    		if(flag){
    			break;
    		}
    		
    		if(array[9] != 0){
    			boolean[] used = new boolean[11];
    			used[array[9]] = true;
    			System.out.println(dfs(0, array, used, array[9]));
    		}else{
    			int sum = 0;
    			boolean[] used = new boolean[11];
    			for(int i = 1; i <= 10; i++){
    				used[i] = true;
    				sum += dfs(0, array, used, i);
    				used[i] = false;
    			}
    			System.out.println(sum);
    		}
    	}
    }
     
}