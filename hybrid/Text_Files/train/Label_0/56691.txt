import java.util.Arrays;
import java.util.Scanner;

public class Main{
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String line = sc.nextLine();
		int n = Integer.valueOf(line.split(" ")[0]);
		int q = Integer.valueOf(line.split(" ")[1]);
		
		int[] array = new int[n];
		Arrays.fill(array, Integer.MAX_VALUE);
		for(int i = 0; i < q; i++){
			String query = sc.nextLine();
			String com = query.split(" ")[0];
			int x = Integer.valueOf(query.split(" ")[1]);
			int y = Integer.valueOf(query.split(" ")[2]);
			switch(com){
				case "0":
					update(array, x, y);
					break;
				case "1":
					System.out.println(findMinimum(array, x, y));
					break;
			}
		}
		sc.close();
	}
	
	static void update(int[] array, int i, int x){
		array[i] = x;
	}
	
	static int findMinimum(int[] array, int from, int to){
		int result = Integer.MAX_VALUE;
		for(int i = from; i <= to; i++){
			if(array[i] < result) result = array[i];
		}
		return result;
	}
}