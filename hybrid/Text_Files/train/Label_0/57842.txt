
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = "";
		try {
			while(true) {
				String s2 = sc.nextLine();
				s += s2;
			}
		}catch(Exception e){}
		char[] chars = s.toCharArray();
		int[] alphabets = new int[26];
		for(char c : chars){
			int unicode = ((int) c);
			if(unicode < 6 * 16){
				unicode += 2 * 16;
			}
			if(96 < unicode && unicode <= 96 + 26){
				alphabets[unicode - 97]++;
			}
		}
		for(int i = 0; i < 26; i++){
			System.out.println((char)(i + 97) + " : " + alphabets[i]);
		}
	}
}

