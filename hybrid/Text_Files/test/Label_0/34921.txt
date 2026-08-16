import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;
 
 
public class Main {
     
	public static final int P_MAX = 100;
	public static final int S_MAX = 10;
	
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] unknown_product = new int[P_MAX];
        int[] unknown_store   = new int[S_MAX];
        
        int[] known_product_sum = new int[P_MAX];
        int[] known_store_sum   = new int[S_MAX];
        
        int[] all_product_sum = new int[P_MAX];
        int[] all_store_sum   = new int[S_MAX];
        
        int[][] table = new int[P_MAX][S_MAX];
        boolean[][] unknown = new boolean[P_MAX][S_MAX];
        
        boolean first = true;
        while(true){
        	final int p = sc.nextInt();
        	
        	if(p == 0){
        		break;
        	}
        	
        	if(!first){
        		System.out.println();
        	}
        	
        	final int s = sc.nextInt();
        	
        	Arrays.fill(unknown_product, 0);
        	Arrays.fill(unknown_store  , 0);
        	Arrays.fill(known_product_sum, 0);
        	Arrays.fill(known_store_sum  , 0);
        	Arrays.fill(all_product_sum, 0);
        	Arrays.fill(all_store_sum  , 0);
        	
        	for(int i = 0; i < p; i++){
        		for(int j = 0; j < s; j++){
        			String input = sc.next();
        			
        			if("?".equals(input)){
        				unknown_product[i]++;
        				unknown_store[j]++;
        				
        				table[i][j] = Integer.MIN_VALUE;
        				unknown[i][j] = true;
        			}else{
        				final int number = Integer.parseInt(input);
        				
        				known_product_sum[i] += number;
        				known_store_sum[j]   += number;
        				table[i][j] = number;
        				unknown[i][j] = false;
        			}
        		}
        		
        		all_product_sum[i] = sc.nextInt();
        	}
        	
        	for(int i = 0; i <= s; i++){
        		final int sum = sc.nextInt();
        		
        		if(i == s){
        			continue;
        		}
        		
        		all_store_sum[i] = sum;
        	}
        	
        	while(true){
        		boolean updated = false;
        		
        		//System.out.println(Arrays.toString(unknown_product));
        		//System.out.println(Arrays.toString(unknown_store));
        		
        		for(int i = 0; i < p; i++){
        			if(unknown_product[i] == 1){
        				
        				for(int j = 0; j < s; j++){
        					if(table[i][j] == Integer.MIN_VALUE){
        						table[i][j] = all_product_sum[i] - known_product_sum[i];
        						unknown_product[i]--;
        						unknown_store[j]--;
        						
        						known_product_sum[i] += table[i][j];
        						known_store_sum[j] += table[i][j];
        						
        						updated = true;
        						break;
        					}
        				}
        				
        			}
        		}
        		
        		for(int i = 0; i < s; i++){
        			if(unknown_store[i] == 1){
        				
        				for(int j = 0; j < p; j++){
        					if(table[j][i] == Integer.MIN_VALUE){
        						table[j][i] = all_store_sum[i] - known_store_sum[i];
        						unknown_store[i]--;
        						unknown_product[j]--;
        						
        						known_store_sum[i] += table[j][i];
        						known_product_sum[j] += table[j][i];
        						
        						updated = true;
        						break;
        					}
        				}
        				
        			}
        		}
        		
        		if(!updated){
        			break;
        		}
        	}
        	
        	boolean flag = true;
        	for(int i = 0; i < p; i++){
        		for(int j = 0; j < s; j++){
        			if(unknown[i][j] && table[i][j] == Integer.MIN_VALUE){
        				flag = false;
        				break;
        			}
        		}
        	}
        	
        	if(!flag){
        		System.out.println("NO");
        	}else{
        		for(int i = 0; i < p; i++){
        			for(int j = 0; j < s; j++){
        				if(unknown[i][j]){
        					System.out.println(table[i][j]);
        				}
        			}
        		}
        	}
        	
        	if(first){
        		first = false;
        	}
        }
    }
 
}