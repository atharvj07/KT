import java.util.*;

public class CodeForces236C{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		long n = input.nextLong();
		if(n == 1){
			System.out.println(1);
		}
		else if(n == 2){
			System.out.println(2);
		}
		else if(n == 3){
			System.out.println(6);
		}
		else{
			if(n%2 == 1){
				System.out.println(n*(n-1)*(n-2));
			}
			else{
				if(n%3 == 0){
					System.out.println((n-1)*(n-2)*(n-3));
				}
				else{
					System.out.println(n*(n-1)*(n-3));
				}
			}
		}
	}
}