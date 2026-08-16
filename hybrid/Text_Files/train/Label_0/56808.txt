import java.util.*;
 
public class Main {
	
    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int x1 = sc.nextInt();
    	int y1 = sc.nextInt();
    	int x2 = sc.nextInt();
    	int y2 = sc.nextInt();
    	int x3 = x2 - (y2 - y1);
    	int y3 = y2 + (x2 - x1);
    	int x4 = x3 - (x2 - x1);
    	int y4 = y3 - (y2 - y1);
    	System.out.println(x3 + " " + y3 + " " + x4 + " " + y4);
    }
}