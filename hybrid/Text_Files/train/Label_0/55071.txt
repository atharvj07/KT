import java.io.PrintWriter;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class PalindromicMatrix {

	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		
		int n = in.nextInt();
		int n2 = n*n;
		int [] arr = new int [n2];
		boolean works = true;
		
		for (int i = 0; i < n2; i++) {
			arr[i] = in.nextInt();
		}
		Arrays.sort(arr);
		int[][] outMat = new int[(n+1)/2][(n+1)/2];

		if (n % 2 == 0) {
			
			int j = 0;
			while (works && j < n2) {
				int current = arr[j];
				if (current != arr[j + 1] || current != arr[j+2] || current != arr[j+3]) {
					works = false;
				}
				j += 4;
			}
			for(int i = 0; i<n/2; i++) {
				for(int k = 0; k<n/2; k++) {
					outMat[i][k] = arr[(i*(n/2)+k)*4];
				}
			}
		}else {
			int ind4 = 0;
			int ind2 = 0;
			int[] part4 = new int[(n/2)*(n/2)];
			int[] part2 = new int[2*(n/2)];
			int oddV = -1;
			for(int i =0; i< n*n;) {
				int st = i;
				i++;
				while(i<n*n && arr[i] == arr[st]) {
					i++;
				}
				
				if((i-st)%2==1) {
					if(oddV==-1) {
						oddV = arr[st];
						st++;
					}
				}
			
				while(st+4<= i && ind4<part4.length) {
					part4[ind4] = arr[st];
					ind4++;
					st+=4;
				}
				while(st+2 <= i && ind2<part2.length) {
					part2[ind2] = arr[st];
					st += 2;
					ind2++;
				}
				if(i!=st) {
					works = false;
				}
			}
			if(oddV==-1) {
				works = false;
			}
			for(int i = 0; i<n/2; i++) {
				for(int j = 0; j<n/2; j++) {
					outMat[i][j] = part4[i*(n/2)+j];
				}
			}
			for (int i = 0; i < n/2; i++) {
				outMat[i][n/2] = part2[i];
			}
			for (int i = n/2; i < 2*(n/2); i++) {
				outMat[n/2][i-n/2] = part2[i];
			}
			outMat[n/2][n/2] = oddV;
		}
		int[][] matrix = new int[n][n];
		for (int i = 0; i < outMat.length; i++) {
			for (int j = 0; j < outMat.length; j++) {
				matrix[i][j] = outMat[i][j];
				matrix[n-1-i][j] = outMat[i][j];
				matrix[i][n-1-j] = outMat[i][j];
				matrix[n-1-i][n-1-j] = outMat[i][j];

			}
		}

		if (works) {
			out.println("YES");
			
			
			printArr(matrix, out);
		} else {
			out.println("NO");
		}
		
		in.close();
		out.close();
	}

	private static void printArr(int[][] matrix, PrintWriter out) {
		
		for (int i = 0; i < matrix.length; i++) {
			for(int j = 0; j < matrix.length - 1; j++) {
				out.print(matrix[i][j]+ " ");
			}
			out.println(matrix[i][matrix.length - 1]);
		}
		
		
		
		
	}

}
