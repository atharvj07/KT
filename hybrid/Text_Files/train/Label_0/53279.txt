import java.util.ArrayList;
import java.util.Scanner;


public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO ツ篠ゥツ督ョツ青カツ青ャツつウツづェツつスツδソツッツドツ・ツスツタツブ
		Scanner sc = new Scanner(System.in);

		ArrayList<String> str = new ArrayList<String>();
		ArrayList<Character> command = new ArrayList<Character>();
		String buf;
		int x=0, y=0;


		while(true){
			buf = sc.nextLine();
			if(buf.equals("END_OF_TEXT")){
				break;
			}
			str.add(buf);
		}
		while(true){
			buf = sc.next();
			if(buf.charAt(0) == '-'){
				break;
			}
			command.add(buf.charAt(0));
		}
		buf = "";

		for(int i=0;i<command.size();i++){
			switch(command.get(i)){
			case 'a'://ok
				x=0;
				break;

			case 'e'://ok
				x=str.get(y).length();
				break;

			case 'p'://ok
				if(y!=0){
					y--;
				}
				x=0;
				break;

			case 'n'://ok
				if(str.size() != y+1){
					y++;
				}
				x=0;
				break;

			case 'f'://ok
				if(str.get(y).length() != x){
					x++;
				}else if(str.size() != y+1){
					y++;
					x=0;
				}
				break;

			case 'b'://ok
				if(x!=0){
					x--;
				}else if(y!=0){
					y--;
					x=str.get(y).length();
				}
				break;

			case 'd'://ok
				if(x!=str.get(y).length()){
					char[] strbuf = str.get(y).toCharArray();
					String resultbuf = "";
					for(int j=0;j<strbuf.length;j++){
						if(x!=j){
							resultbuf += strbuf[j];
						}
					}
					str.set(y,resultbuf);
				}else if(str.size() != y+1){
					str.set(y, str.get(y)+str.get(y+1));
					str.remove(y+1);
				}
				break;

			case 'k'://ok
				if(x!=str.get(y).length()){
					char[] strbuf = str.get(y).toCharArray();
					String resultbuf = "";
					buf = "";
					for(int j=0;j<strbuf.length;j++){
						if(x>j){
							resultbuf += strbuf[j];
						}else{
							buf += strbuf[j];
						}
					}
					str.set(y,resultbuf);
					x = str.get(y).length();
				}else if(str.size() != y+1){
					buf = "\n";
					str.set(y, str.get(y)+str.get(y+1));
					str.remove(y+1);
				}
				break;

			case 'y':
				if(buf.equals("\n")){
					char[] strbuf = str.get(y).toCharArray();
					String resultbuf = "";
					buf = "";
					for(int j=0;j<strbuf.length;j++){
						if(x>j){
							resultbuf += strbuf[j];
						}else{
							buf += strbuf[j];
						}
					}
					str.set(y,resultbuf);
					str.add(y+1,buf);

					y++;
					x=0;
					buf="\n";
				}else if(buf.length() != 0){
					char[] strbuf = str.get(y).toCharArray();
					String resultbuf = "";
					for(int j=0;j<=strbuf.length;j++){
						if(x==j){
							resultbuf += buf;
						}
						if(j!=strbuf.length){
							resultbuf += strbuf[j];
						}
					}
					str.set(y, resultbuf);
					x+=buf.length();
				}
				break;
			}
		}
		for(int i=0;i<str.size();i++){
			System.out.println(str.get(i));
		}
	}

}