import java.util.ArrayList;
import java.util.Scanner;

 
public class Main {
 
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int n  = sc.nextInt();
		int k  = sc.nextInt();
		int r  = sc.nextInt();
		int s  = sc.nextInt();
		int p  = sc.nextInt();
		char[] tArray = sc.next().toCharArray(); 
        int ans = 0;
        
        for(int i = 0; i < n; i++) {
        	if(i < k) {
            	if(tArray[i] == 's') {
            		ans += r;
            	}else if(tArray[i] == 'p') {
            		ans += s;
            	}else if(tArray[i] == 'r') {
            		ans += p;
            	}
        	}else {
        		if(tArray[i] != tArray[i - k]){
                	if(tArray[i] == 's') {
                		ans += r;
                	}else if(tArray[i] == 'p') {
                		ans += s;
                	}else if(tArray[i] == 'r') {
                		ans += p;
                	}
        		}else {
        			tArray[i] = '0';
        		}
        	}
        }

		System.out.println(ans);
		sc.close();
	}

}