import java.util.Collections;
import java.util.ArrayList;
import java.lang.Math;
import java.util.Scanner;

public class CF735B{
	public static double getAnswer(int n, int n1, int n2, ArrayList<Integer> a){
		Collections.sort(a, Collections.reverseOrder());
		
		Double total1 = 0.0;
		Double total2 = 0.0;
		int index = 0;

		int min = Math.min(n1,n2);
		int max = Math.max(n1,n2);

		for(int i = 0; i < min; ++i){
			// total1 *= i;
			total1 += a.get(index);
			// total1 /= i+1;
			++index;
		}

		for(int j = 0; j < max; ++j){
			total2 += a.get(index);
			++index;
		}

		return total1/min + total2/max;
	}

	public static void main(String[] args){
		Scanner in = new Scanner(System.in);

		// getting inputs
		int n = in.nextInt();
		int n1 = in.nextInt();
		int n2 = in.nextInt();
		ArrayList<Integer> a = new ArrayList<Integer>();
		for(int i = 0; i < n; ++i){
			a.add(in.nextInt());
		}

		// call solution and print the answer
		System.out.println(getAnswer(n, n1, n2, a));
	}
}