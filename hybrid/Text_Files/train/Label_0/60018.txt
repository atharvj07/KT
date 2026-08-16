
import java.awt.geom.*;
import java.util.*;
public class Main {
	//2142 start
	//2202 stop
	//2346 restart
	
	HashMap<String, Integer> table;
	ArrayList<C> list;
	
	class C implements Comparable<C>{
		int value, len;
		String s;
		public C( String s, int value) {
			this.value = value;
			this.s = s;
			this.len = s.length();
		}
		@Override
		public int compareTo(C o) {
			if(this.len < o.len) return 1;
			if(this.len > o.len) return -1;
			return 0;
		}
		
	}
	
	private void doit(){
		Scanner sc = new Scanner(System.in);
		table = new HashMap<String, Integer>();
		list = new ArrayList<Main.C>();
		while(true){
			String s = sc.next();
			if(s.equals("END_OF_FIRST_PART")) break;
			int num = sc.nextInt();
			table.put(s, num);
			C temp = new C(s, num);
			list.add(temp);
		}
		Collections.sort(list);
		
		while(true){
			String s = sc.next();
			if(s.equals("0")) break;
			int res = eval(s);
			if(res < 0) System.out.println("UNKNOWN");
			else{
				System.out.println(res);
			}
		}
	}

	private int eval(String str) {
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < str.length(); i++){
			char c = str.charAt(i);
			if(i == 0 || str.charAt(i -1) == '(' || c == ')'){
				
			}
			else if('a' <= c && c <= 'z'){
				
			}
			else if(Character.isDigit(c)){
				sb.append('*');
				for(; i+1 < str.length(); i++){
					if(Character.isDigit(str.charAt(i+1))){
						sb.append(str.charAt(i));
					}
					else{
						break;
					}
				}
			}
			else {
				
				sb.append('+');
			}
			sb.append(str.charAt(i));
		}
		String s = sb.toString();
		for(int i = 0; i < list.size(); i++){
			s = s.replaceAll(list.get(i).s, list.get(i).value + "");
		}
		for(int i = 0; i < s.length(); i++){
			char c = s.charAt(i);
			if(Character.isLetter(c)){
				return -1;
			}
		}
		return new Parse(s+"#").exp();
	}
	
	class Parse{
		String str;
		int pos;
		public Parse(String str){
			this.str = str;	pos = 0;
		}
		
		private int exp() {
			int res = term();
			while(true){
				char op = str.charAt(pos);
				if((op == '+') || (op == '-')){
					int old = res;
					pos++;
					res = term();
					switch(op){
					case '+': 
						res = old + res;
						break;
					case '-':
						res = old - res;
						break;
					}
				}
				else break;
			}
			return res;
		}

		private int term() {
			int res = fact();
			while(true){
				char op = str.charAt(pos);
				if((op == '*') || (op == '/')){
					int old = res;
					pos++;
					res = fact();
					switch(op){
					case '*':
						res = old * res;
						break;
					case '/':
						res = old / res;
						break;
					}
				}
				else break;
			}
			return res;
		}

		private int fact() {
			if(Character.isDigit(str.charAt(pos))){
				int t = str.charAt(pos) - '0';
				pos++;
				while(Character.isDigit(str.charAt(pos))){
					t = t * 10 + (str.charAt(pos) - '0');
					pos++;
				}
				return t;
			}
			else if(str.charAt(pos) == '('){
				pos++;
				int res = exp();
				pos++;
				return res;
			}
			return 0;
		}
	}

	public static void main(String[] args) {
		Main obj = new Main();
		obj.doit();
	}
}