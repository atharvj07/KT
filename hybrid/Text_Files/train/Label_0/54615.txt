import java.util.Scanner;

public class Main {
    public static void main(String[] args){
    	Scanner in = new Scanner(System.in);
    	int i = in.nextInt();
    	for(int j = 0;j < i;j++){
    		int a = in.nextInt();
    		int b = in.nextInt();
    		int c = in.nextInt();
    		a = a * a;
    		b = b * b;
    		c = c * c;
    		if(a == b + c || b == a + c || c == b + a){
    			System.out.println("YES");
    		}
    		else{
    			System.out.println("NO");
    		}
    	}
    }
}