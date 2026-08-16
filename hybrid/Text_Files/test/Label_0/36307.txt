import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		int n = stdIn.nextInt();
		int a[] = new int[n];
		for(int i = 0; i < n; i++){
		    a[i] = stdIn.nextInt();
		}
		
		int m = stdIn.nextInt();
		int num[] = new int[n + m];
		for(int i = 0; i < n + m; i++){
		    if(i < n){
		        num[i] = a[i];
		    }else{
		        num[i] = stdIn.nextInt();
		    }
		}
		
		Arrays.sort(num);
        
        for(int i = 0; i < n + m; i++){
            if(i == 0){
                if(num[i] != num[i + 1]){
                    System.out.println(num[i]);
                }
            }else if(i == n + m - 1){
                if(num[i - 1] != num[i]){
                    System.out.println(num[i]);
                }
            }else{
                if(num[i - 1] != num[i] && num[i] != num[i + 1]){
                    System.out.println(num[i]);
                }
            }
            
        }
        
		stdIn.close();
	}

}


