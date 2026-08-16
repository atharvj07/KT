import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		    Scanner sc = new Scanner(System.in);

		    int max = 0;
		    int max_num =0;
		    int max2 = 0;
		    int n = sc.nextInt();
		    for(int i=0; i<n; i++) {
		    	int a = sc.nextInt();
		    	if(a>max) {
		    		max = a;
		    		max_num = i;
		    	}else {
		    		if(a>=max2) {
		    			max2 = a;
		    		}
		    	}
		    }
		    for(int i=0; i<n; i++) {
		    	if(i==max_num) {
		    		System.out.println(max2);
		    	}else {
		    		System.out.println(max);
		    	}
		    }
		    sc.close();

	}
}