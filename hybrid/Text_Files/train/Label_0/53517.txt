import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int[] s = new int[n];
		for(int i=0; i<n; i++){
			s[i] = in.nextInt();
		}
		Set<Integer> list = new HashSet<>();
		for(int i=1; i*i<=n; i++){
			if(n%i==0){
				list.add(i);
				list.add(n/i);
			}
		}
		list.remove(n);
		int max = 1;
		out:for(int t: list){
			for(int i=0; i<n-t; i++){
				if(s[i] != s[i+t]) continue out;
			}
			max = Math.max(n/t, max);
		}
		System.out.println(max);
	}
}