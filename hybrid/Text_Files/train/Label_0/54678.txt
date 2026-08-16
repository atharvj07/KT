

import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] array = new long[n+1];
		array[0] = 2; array[1] = 1;
		for(int i = 2;i <= n;++i){
			array[i] = array[i-1] + array[i-2]; 
		}
		System.out.println(array[n]);
	}
}
