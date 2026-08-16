import java.io.*;
import java.util.*;
public class ants_circle {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken()); 
		int M = Integer.parseInt(st.nextToken()); 
		long T = Long.parseLong(st.nextToken()); 

		
		int[][] ants = new int[N][4];
		int totalSpeed = 0;

		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			ants[i][0] = Integer.parseInt(st.nextToken())%M;


			char dir = st.nextToken().charAt(0);
			ants[i][1] = dir=='L' ? -1 : 1; 

			ants[i][2] = i; 

			totalSpeed += ants[i][1];
			

		}

		Arrays.sort(ants, (a, b) -> a[0] - b[0]);


		int[] q = new int[N];
		for(int i=0; i<N; i++) {
			q[i] = (int) (ants[i][0] + (ants[i][1] * (T%M) % M)) % M;
			if(q[i]<0) q[i] += M;
		}
		Arrays.sort(q);
		
		long NM = (long)N*M;
		
		long sT = 0;
		for(int j=0; j<Math.abs(totalSpeed); j++) {
			sT += T;
			sT %= NM;
		}
		if(totalSpeed<0) sT = -sT;
		
		long totalDisplacement = 0;
		for(int j=0; j<N; j++) {
			totalDisplacement += (q[j] - ants[j][0]);
			totalDisplacement %= (NM);
		}
		
		int x = (int)((sT-totalDisplacement)/M);
		if(x<0)
			x += N;
		
		for(int i=0; i<N; i++) {
			ants[i][3] = q[(i+x)%N];
			if(ants[i][3]==0) ants[i][3] = M;
		}

		Arrays.sort(ants, (a, b) -> a[2]-b[2]);

		for(int i=0; i<N; i++)
			System.out.print(ants[i][3] + " ");
		System.out.println();

		br.close();
	}
}