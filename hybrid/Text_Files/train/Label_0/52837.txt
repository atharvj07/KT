import java.util.Scanner;

public class Main {

	public static void main(String []args){
		
		Scanner in = new Scanner(System.in);
		
		int n = in.nextInt();
		
		int[] votes = new int[n];
		for(int i = 0; i < n; i++){
			votes[i] = (int)(Math.random()*1000 + 1);
			votes[i] = in.nextInt();
		}
		
		int mvotes = votes[0];
		
		int maxvotes = 0;
		for(int i = 1; i < n; i++)
			if(votes[i] > maxvotes)
				maxvotes = votes[i];
		
		if(mvotes > maxvotes){
			System.out.println(0);
			return;
		}
		
		int needtobuy = 0;
		
		while(mvotes <= findMax(votes)[1]){
			mvotes++;
			votes[findMax(votes)[0]]--;
			needtobuy++;
		}
		
		System.out.println(needtobuy);
	}
	
	private static int[] findMax(int[] a){
		int []maxj = new int[2];
		maxj[1] = 0;
		maxj[0] = 0;
		for(int i = 1; i < a.length; i++){
			if(a[i] > maxj[1]){
				maxj[1] = a[i];
				maxj[0] = i;
			}
		}
		return maxj;
	}
}
