import java.util.*;

public class B {
	
	static Scanner k = new Scanner(System.in);
	static int [] y;
	
    public static void main(String[] args){
    	while(k.hasNext()){
    		y = new int[k.nextInt()];
    		for(int i = 0; i<y.length; i++){
    			y[i] = k.nextInt();
    		}
    		
    		Arrays.sort(y);
    		long sum = 0;
    		for(int i = 0; i<y.length - 1; i+=2){
    			sum += (y[i+1] - y[i]);
    		}
    		
    		System.out.println(sum);
    	}
    }

}