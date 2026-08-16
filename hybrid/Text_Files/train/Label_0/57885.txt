import java.util.Scanner;
public class Hulk2{
	public static void main(String[]args){
		Scanner apple = new Scanner(System.in);
		int n = apple.nextInt();
		int i;
		   for (i = 0; i < n; i++) {
            if (i % 2 == 0) {
                System.out.printf("I hate ");
            }
            else {
                System.out.printf("I love ");
            }
            if (i < n - 1) {
                System.out.printf("that ");
            }
        }
        System.out.printf("it");
}
}