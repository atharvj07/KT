import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;


public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNext()){
			final int n = sc.nextInt();
			final int r = sc.nextInt();
			
			int[] array = new int[n];
			for(int i = 0; i < n; i++){
				array[i] = i;
			}
			
			for(int i = 0; i < r; i++){
				
				int c = sc.nextInt();
				
				LinkedList<Integer> A = new LinkedList<Integer>();
				LinkedList<Integer> B = new LinkedList<Integer>();
				LinkedList<Integer> C = new LinkedList<Integer>();
				
				for(int j = 0; j < n; j++){
					if(j <= (n / 2 - 1)){
						B.addLast(array[j]);
					}else{
						A.addLast(array[j]);
					}
				}
				
				while(!A.isEmpty() || !B.isEmpty()){
					int size = A.size();
					for(int j = 0; j < Math.min(c, size); j++){
						C.addLast(A.poll());
					}
					
					size = B.size();
					for(int j = 0; j < Math.min(c, size); j++){
						C.addLast(B.poll());
					}
				}
				
				int index = 0;
				for(int num : C){
					array[index++] = num;
				}
			}
			
			
			System.out.println(array[n - 1]);
		}
	}

}