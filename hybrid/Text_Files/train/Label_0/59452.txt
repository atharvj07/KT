import java.util.*;

public class Main {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	int a;
	boolean result = true;
	for (int i=0; i<n; i++) {
	    a = sc.nextInt();
	    if (a % 2 == 0) {
		if (!(a % 3 == 0 || a % 5 == 0)) {
		    result = false;
		    break;
		}
	    }
	}
	System.out.print(result ? "APPROVED" : "DENIED");
    }
}
