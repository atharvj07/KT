
import java.util.ArrayList;
import java.util.Scanner;

//this implements the shell sort algorithm
public class Main {
	public static int cnt = 0;
	// do insertion sort with a given interval
	
	public static void insertion_sort(int[] arr, int inv) {
		int n = arr.length;
		for(int i = inv; i < n; i ++) {
			int key = arr[i];
			int j = i - inv;
			
			while( j >= 0 && arr[j] > key) {
				arr[j+inv] = arr[j]; // do the shift
				j -= inv;
				cnt++;
			}
			
			arr[j+inv] = key;
		}
	}
	
	
	// we will also use the g_{n+1} = 3*g_{n} + 1 
	
	//give the array length, generate a possible list of interval's according to the recurrent relation above
	public static ArrayList<Integer> generate_inv(int n) {
		ArrayList<Integer> invs = new ArrayList<Integer>();
		
		int q = 1;
		while(q <= n) {
			invs.add(q);
			q = 3*q+1;
		}
		
		return invs;
	}
	
	
	public static void main(String [] args) {
		Scanner cin = new  Scanner(System.in);
		int n = cin.nextInt();
		int [] arr = new int[n];
		
		//read in the array
		for(int i = 0; i < n; i++) {
			arr[i] = cin.nextInt();
		}
		
		ArrayList<Integer> invs = generate_inv(n);
		
		System.out.println(invs.size());
		
		for(int i = invs.size()-1; i >= 0; i--) {
			System.out.print(invs.get(i));
			if(i == 0) {
				System.out.print("\n");
			}else {
				System.out.print(" ");
			}
			insertion_sort(arr, invs.get(i));
		}
		
		//finally output cnt
		System.out.println(cnt);
		for(int i = 0; i < arr.length; i++) {
			System.out.print(arr[i]);
			
			if(i < arr.length -1) {
				System.out.print("\n");
			}
		}
		
		cin.close();
		
	}
	
}