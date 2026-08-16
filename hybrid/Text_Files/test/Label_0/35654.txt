import java.util.Scanner;

public class Main{
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		while(scan.hasNext()){
			String str = scan.next();
			if(str.equals("#")){
				break;
			}
			char city = 'A';
			for(int i = 0;i < str.length();i++){
				city = ans(city,str.charAt(i));
			}
			System.out.println((city == 'B')?"Yes":"No");
		}
	}
	
	public static char ans(char city,char road){
		switch(city){
		case 'A':
			return (road=='0')?'X':'Y';
		case 'B':
			return (road=='0')?'Y':'X';
		case 'X':
			return (road=='0')?'M':'Z';
		case 'Y':
			return (road=='0')?'X':'M';
		case 'W':
			return (road=='0')?'B':'Y';
		case 'Z':
			return (road=='0')?'W':'B';
		}
		return city;
	}
}