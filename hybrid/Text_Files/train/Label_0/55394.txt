import java.util.Scanner;
public class Main {
private static Scanner s = new Scanner(System.in);
private static int[] a = new int[45];
public static void main(String[] args) {

int n = s.nextInt();
fibonacci(n);
System.out.println(a[n]);
}

static void fibonacci(int n) {
	a[0] = 1;
	a[1] = 1;
	for(int i = 2;i <= n;i++) {
		a[i] = a[i-2] + a[i-1];
	}
}
}
