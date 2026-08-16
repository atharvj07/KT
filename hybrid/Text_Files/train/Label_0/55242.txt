import java.io.*;
import java.util.*;

public class AntiSudoku {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(in.readLine());
		for (int t = 0; t < T; t++) {
			String[] lines = new String[9];
			
			for (int i = 0; i < 9; i++)
				lines[i] = in.readLine();
			
			lines[0] = replace(lines[0], 0);
			lines[1] = replace(lines[1], 3);
			lines[2] = replace(lines[2], 6);
			
			lines[3] = replace(lines[3], 1);
			lines[4] = replace(lines[4], 4);
			lines[5] = replace(lines[5], 7);
		
			lines[6] = replace(lines[6], 2);
			lines[7] = replace(lines[7], 5);
			lines[8] = replace(lines[8], 8);
			
			for (int i = 0; i < 9; i++)
				System.out.println(lines[i]);
		}
	}
	public static String replace(String str, int i) {
		return str.substring(0, i) + (((str.charAt(i) - '0')  % 9) + 1) + str.substring(i+1, str.length());
	}
}
