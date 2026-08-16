import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

//The Code A Doctor Loved
public class Main {

	public static void main(String[] args) {
		Map<Character, String> t = new HashMap<Character, String>();
		t.put(' ', "101");
		t.put('\'', "000000");
		t.put(',', "000011");
		t.put('-', "10010001");
		t.put('.', "010001");
		t.put('?', "000001");
		t.put('A', "100101");
		t.put('B', "10011010");
		t.put('C', "0101");
		t.put('D', "0001");
		t.put('E', "110");
		t.put('F', "01001");
		t.put('G', "10011011");
		t.put('H', "010000");
		t.put('I', "0111");
		t.put('J', "10011000");
		t.put('K', "0110");
		t.put('L', "00100");
		t.put('M', "10011001");
		t.put('N', "10011110");
		t.put('O', "00101");
		t.put('P', "111");
		t.put('Q', "10011111");
		t.put('R', "1000");
		t.put('S', "00110");
		t.put('T', "00111");
		t.put('U', "10011100");
		t.put('V', "10011101");
		t.put('W', "000010");
		t.put('X', "10010010");
		t.put('Y', "10010011");
		t.put('Z', "10010000");
		Map<String, Character> r = new HashMap<String, Character>();
		r.put("00000", 'A');
		r.put("00001", 'B');
		r.put("00010", 'C');
		r.put("00011", 'D');
		r.put("00100", 'E');
		r.put("00101", 'F');
		r.put("00110", 'G');
		r.put("00111", 'H');
		r.put("01000", 'I');
		r.put("01001", 'J');
		r.put("01010", 'K');
		r.put("01011", 'L');
		r.put("01100", 'M');
		r.put("01101", 'N');
		r.put("01110", 'O');
		r.put("01111", 'P');
		r.put("10000", 'Q');
		r.put("10001", 'R');
		r.put("10010", 'S');
		r.put("10011", 'T');
		r.put("10100", 'U');
		r.put("10101", 'V');
		r.put("10110", 'W');
		r.put("10111", 'X');
		r.put("11000", 'Y');
		r.put("11001", 'Z');
		r.put("11010", ' ');
		r.put("11011", '.');
		r.put("11100", ',');
		r.put("11101", '-');
		r.put("11110", '\'');
		r.put("11111", '?');
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			char[] s = sc.nextLine().toCharArray();
			StringBuilder sb = new StringBuilder();
			for(char c:s)sb.append(t.get(c));
			while(sb.length()%5!=0)sb.append('0');
			String u = sb.toString();
			StringBuilder v = new StringBuilder();
			for(int i=0;i<u.length();i+=5)v.append(r.get(u.substring(i, i+5)));
			System.out.println(v);
		}
	}
}