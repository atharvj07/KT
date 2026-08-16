import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		final char[] THE = {'t', 'h', 'e'};
		final char[] THIS = {'t', 'h', 'i', 's'};
		final char[] THAT = {'t', 'h', 'a', 't'};
		while(sc.hasNext()){
			char[] charset = sc.nextLine().toCharArray();
			for (int i = 0; i <= (int)('z'-'a'); i++){
				if (isMatch(charset, THE)
						|| isMatch(charset, THIS)
						|| isMatch(charset, THAT)){
					System.out.println(charset);
					break;
				}
				charset = charshift(charset, 'a', 'z');
			}
		}
		sc.close();
	}
	
	private static boolean isMatch(char[] c, char[] pattern){
		boolean res = false;
		for (int i = 0; i < c.length - pattern.length + 1; i++){
			boolean flag = true;
			for (int j = 0; j < pattern.length; j++){
				flag = flag && (c[i+j] == pattern[j]);
			}
			if(flag){
				res = flag;
				break;
			}
		}
		return res;
	}
	
	private static char[] charshift(char[] c, char start, char end){
		char[] res = new char[c.length];
		for (int i=0; i < c.length; i++){
			if(c[i]>= start && c[i]< end){
				res[i] = (char)((int)c[i] + 1);
			}else if(c[i] == end){
				res[i] = start;
			}else{
				res[i] = c[i];
			}
		}
		return res;
	}
}