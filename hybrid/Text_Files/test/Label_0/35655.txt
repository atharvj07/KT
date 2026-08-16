import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.TreeSet;
 
 
public class Main{
     
    public static void main(String[] args) throws IOException {
    	Scanner sc = new Scanner(System.in);
    	
    	final int m = sc.nextInt();
    	
    	HashMap<String, ArrayList<Boolean>> v_map = new HashMap<String, ArrayList<Boolean>>();
        
    	for(int i = 0; i < m; i++){
    		final String name = sc.next();
    		final int low = sc.nextInt();
    		final int high = sc.nextInt();
    		
    		ArrayList<Boolean> list = new ArrayList<Boolean>(256);
    		for(int j = 0; j < 256; j++){
    			if(j < low || j > high){
    				list.add(false);
    			}else{
    				list.add(true);
    			}
    		}
    		
    		v_map.put(name, list);    		
    	}
    	
    	final int n = sc.nextInt();
    	
    	LinkedList<ArrayList<Boolean>> stack = new LinkedList<ArrayList<Boolean>>();
    	
    	for(int i = 0; i < n; i++){
    		final String input = sc.next();
    		
    		//System.out.println(stack);
    		
    		try{
    			int num = Integer.parseInt(input);
    			
    			ArrayList<Boolean> list = new ArrayList<Boolean>(256);
        		for(int j = 0; j < 256; j++){
        			if(j == num){
        				list.add(true);
        			}else{
        				list.add(false);
        			}
        		}
        		
        		stack.push(list);
    			
    		}catch(NumberFormatException e){
    			if("+".equals(input)){
    				ArrayList<Boolean> b = stack.poll();
    				ArrayList<Boolean> a = stack.poll();
    				ArrayList<Boolean> ans = new ArrayList<Boolean>(256);
    				
    				for(int j = 0; j < 256; j++){
    					ans.add(false);
    				}
    				
    				for(int j = 0; j < 256; j++){
    					if(!a.get(j)){
    						continue;
    					}
    					
    					for(int k = 0; k < 256; k++){
    						if(!b.get(k)){
    							continue;
    						}
    						
    						ans.set((j + k) % 256 , true);
    					}
    				}
    				
    				stack.push(ans);
    			}else if("-".equals(input)){
    				ArrayList<Boolean> b = stack.poll();
    				ArrayList<Boolean> a = stack.poll();
    				ArrayList<Boolean> ans = new ArrayList<Boolean>(256);
    				
    				for(int j = 0; j < 256; j++){
    					ans.add(false);
    				}
    				
    				for(int j = 0; j < 256; j++){
    					if(!a.get(j)){
    						continue;
    					}
    					
    					for(int k = 0; k < 256; k++){
    						if(!b.get(k)){
    							continue;
    						}
    						
    						ans.set((j - k + 256) % 256 , true);
    					}
    				}
    				
    				stack.push(ans);
    			}else if("/".equals(input)){
    				ArrayList<Boolean> b = stack.poll();
    				ArrayList<Boolean> a = stack.poll();
    				ArrayList<Boolean> ans = new ArrayList<Boolean>(256);
    				
    				for(int j = 0; j < 256; j++){
    					ans.add(false);
    				}
    				
    				for(int j = 0; j < 256; j++){
    					if(!a.get(j)){
    						continue;
    					}
    					
    					for(int k = 0; k < 256; k++){
    						if(!b.get(k)){
    							continue;
    						}
    						
    						if(k == 0){
    							System.out.println("error");
    							return;
    						}
    						
    						ans.set((j / k) % 256 , true);
    					}
    				}
    				
    				stack.push(ans);
    			}else if("*".equals(input)){
    				ArrayList<Boolean> b = stack.poll();
    				ArrayList<Boolean> a = stack.poll();
    				ArrayList<Boolean> ans = new ArrayList<Boolean>(256);
    				
    				for(int j = 0; j < 256; j++){
    					ans.add(false);
    				}
    				
    				for(int j = 0; j < 256; j++){
    					if(!a.get(j)){
    						continue;
    					}
    					
    					for(int k = 0; k < 256; k++){
    						if(!b.get(k)){
    							continue;
    						}
    						
    						ans.set((j * k) % 256 , true);
    					}
    				}
    				
    				stack.push(ans);
    			}else{
    				stack.push(v_map.get(input));
    			}
    			
    			
    		}
    	}
    	//System.out.println(stack);
    	System.out.println("correct");
    }
     
}