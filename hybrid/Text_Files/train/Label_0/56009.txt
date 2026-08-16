import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner stdIn = new Scanner(System.in);
		int N = stdIn.nextInt();
		ArrayList<Integer> A = new ArrayList<Integer>();
		for(int i = 0; i < N; i ++) {
			A.add(stdIn.nextInt());
		}
		
		long stepSum = 0;
		
		for(int i = 1; i < N; i ++) {
			if(A.get(i - 1) <= A.get(i)) {
				continue;
			}else {
				stepSum += A.get(i - 1) - A.get(i);
				A.set(i, A.get(i - 1));
			}
		}
		
		System.out.println(stepSum);
	}
}