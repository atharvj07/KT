import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		char[] s = sc.next().toCharArray();
		int len = 0;
		for(int i=0;i<s.length;i++) {
			if (len % 2 == 0 && s[i] == 'A' || len % 2 == 1 && s[i] == 'Z') {
				len++;
			}
		}
		len /= 2;
		if (len == 0) {
			System.out.println(-1);
		}else{
			StringBuilder sb = new StringBuilder();
			for(int i=0;i<len;i++) {
				sb.append("AZ");
			}
			System.out.println(sb.toString());
		}
	}

}