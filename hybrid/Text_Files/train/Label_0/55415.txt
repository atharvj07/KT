import java.util.*;
public class Main {
    public static void main(String[] args){
    
        Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		HashSet<Integer> a = new HashSet<>();
		int A = 0;
		
		for(int i = 0; i < N; i++) {
			A=sc.nextInt();
			a.add(A);
		}
		
		if(a.size() == N) {
			System.out.println("YES");
		}else {
			System.out.println("NO");
		}
    }
}