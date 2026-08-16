import java.io.*;
import java.util.*;

public class Azembler {

	static int[] registers;
	static int[] k = {1, 2, 4, 8};
	
	static String regChars = "abcdefghijklmnopqrstuvwxyz";
	
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int number = Integer.parseInt(in.readLine());
		
		registers = new int[30];
		registers[0] = 1;
		for (int i = 0;; i++) {
			if (find(1, number, 0, i)) {
				System.out.println(i);
				createProgram(i);
				return;
			}
		}
	}
	
	static void createProgram(int len) {
		start:
		for (int i = 1; i <= len; i++) {
			for (int j = 0; j < i; j++) {
				for (int m = 0; m < 4; m++) {
					int num = registers[j] * k[m];
					if (num == registers[i]) {
						System.out.println("lea "+getReg(i)+", ["+k[m]+"*"+getReg(j)+"]");
						continue start;
					}
					for (int n = 0; n < i; n++) {
						if (registers[n] + num == registers[i]) {
							System.out.println("lea "+getReg(i)+", ["+getReg(n)+" + "+k[m]+"*"+getReg(j)+"]");
							continue start;
						}
					}
				}
			}
		}
	}
	
	static String getReg(int i) {
		return "e"+regChars.charAt(i)+"x";
	}
	
	static boolean find(int curr, int goal, int dep, int max) {
		if (dep == max) {
			if (curr == goal) {
				return true;
			} else {
				return false;
			}
		}
		if (curr > goal) return false;
		for (int i = 0; i <= dep; i++) {
			for (int m = 0; m < 4; m++) {
				int num = k[m]*registers[i];
				registers[dep + 1] = num;
				if (find(num, goal, dep + 1, max)) return true;
				for (int j = 0; j <= dep; j++) {
					registers[dep + 1] = registers[j] + num;
					if(find(registers[j] + num, goal, dep + 1, max)) return true;
				}
			}
		}
		return false;
	}
}
