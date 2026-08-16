import java.util.*;
import java.io.*;
 
public class Main{
    
	public static void main(String[] $){
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		long sum = 0;
		long[] S = new long[100000+1];
		for(int i = 0; i < N; i++){
			int A = s.nextInt();
			sum += A;
			S[A]++;
		}

		int Q = s.nextInt();
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < Q; i++){
			int B = s.nextInt();
			int C = s.nextInt();
			int result = C - B;
			sum = sum + S[B]*result;
			S[C] = S[C] + S[B];
			S[B] = 0;
			sb.append(sum + "\n");
		}
		System.out.print(sb.toString());
		
		
			
	}
} 