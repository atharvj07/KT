import java.util.Scanner;

public class Main{
	
	private static int[] A;

	public static void main(String[] args) {
		int n;
		Scanner in = new Scanner(System.in);
		n = in.nextInt();
		A = new int[n];
		for(int i = 0; i < n; i ++) {
			A[i] = in.nextInt();
		}
		in.close();
		
		
		buildMaxHeap();
		printHeap();
		
	}
	
	public static void maxHeapify(int[] A, int i) {
		int largest = i;
		int l = 2*i + 1;
		int r = 2*i + 2;
		
		if (l < A.length && A[l] > A[largest]) {
			largest = l;
		}
		
		if (r < A.length && A[r] > A[largest]) {
			largest = r;
		}
		
		if (largest != i) {
			int temp = A[i];
			A[i] = A[largest];
			A[largest] = temp;
			maxHeapify(A, largest);
		}
		
	}
	
	public static void buildMaxHeap() {
		for (int i = (A.length / 2) - 1; i >= 0; i--) {
			maxHeapify(A, i);	
		}
	}
	
	public static void printHeap() {
		for (int i = 0; i < A.length; i++) {
			System.out.print(" "+ A[i]);
		}
System.out.println();
	}

}
