import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main{
	public static void main(String args[]) throws IOException {
		Scanner scan = new Scanner(System.in);

		String line = scan.nextLine();
		//int N = Integer.parseInt(line);
		
		float[] A = new float[2];
		float[] B = new float[2];
		float[] C = new float[2];
		float[] D = new float[2];
		
		List<Boolean> L = new ArrayList<Boolean>();
		
		while(scan.hasNext()){
			line = scan.nextLine();
			String[] s = line.split(" +");
			A[0] = Float.parseFloat(s[0]);
			A[1] = Float.parseFloat(s[1]);
			
			B[0] = Float.parseFloat(s[2]);
			B[1] = Float.parseFloat(s[3]);
			
			C[0] = Float.parseFloat(s[4]);
			C[1] = Float.parseFloat(s[5]);
			
			D[0] = Float.parseFloat(s[6]);
			D[1] = Float.parseFloat(s[7]);
			
			float AB = (B[1] - A[1])/(B[0] - A[0]);
			float CD = (D[1] - C[1])/(D[0] - C[0]);;
		    L.add(AB == CD);
		}

		for(Boolean Li : L) {
			System.out.println(Li?"YES":"NO");
		}
		
		scan.close();
	}
}
