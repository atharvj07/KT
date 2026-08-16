import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int[] h = new int[n];
		for (int i = 0; i < n; i++)
			h[i] = in.nextInt();
		
		System.out.println(water(h, 0, n - 1));		

	}
	
	public static int water(int[] h, int left, int right){

		if (right < left)
			return 0;
		else {
			int min = h[left];
			for (int i = left; i <= right; i++) 
				min = Math.min(min,	h[i]);
			for (int i = left; i <= right; i++)
				h[i] -= min;
			for (int i = left; i <= right; i++) {
				if (h[i] == 0)
					return min + water(h, left, i - 1) + water(h, i + 1, right);
			}
			
		}
		return 0;

	}

}