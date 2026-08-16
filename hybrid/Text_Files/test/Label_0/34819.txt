import java.io.*;
import java.util.*;
 
public class Main {
    public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
        try {
            int A_size;
            
            while(true){
                boolean nosol = true;
                long res = 0;
                /* input from here */
                A_size = s.nextInt();
                if(A_size==0){
                    break;
                } else if(A_size==1){
                    System.out.println(s.nextInt());
                    continue;
                } else {
                	HashMap<Long,Integer> A = new HashMap<Long,Integer>();
                    for(int i=0;i<A_size;i++){
                        long t = s.nextLong();
                        if(A.containsKey(t)){
                        	int v = A.get(t);
                        	if(v+1>A_size/2){
                        		res = t;
                        		nosol = false;
                        	}
                        	A.put(t, v+1);                        	
                        } else {
                        	A.put(t,1);
                        }
                        if(i % 30000 == 0) System.gc();
                    }
                }
                /* input till here */
                if(nosol){
                    System.out.println("NO COLOR");
                } else {
                	System.out.println(res);
                }
                 
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
        	s.close();
        }
    }
}