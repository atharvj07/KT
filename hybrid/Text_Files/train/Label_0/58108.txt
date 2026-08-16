import java.util.Scanner;

class Main {

    static long lcm (long a, long b) {
	long temp;
	long c = a;
	c *= b;

	while((temp = a % b) != 0) {
	    a = b;
	    b = temp;
	}

	return c / b;
    }
    
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);

	long A, B;
	A = sc.nextLong();
	B = sc.nextLong();

	System.out.println(lcm(A, B));
    }
}