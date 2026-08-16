
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String s = scanner.next();
		String[] s2 = s.split("e");
		String pre = s2[0];
		String sub = s2[1];
		
		int subInt = Integer.valueOf(sub);
		if (subInt == 0){
			if (pre.endsWith(".0")){
				System.out.println(pre.substring(0, pre.indexOf('.')));
			}else{
				System.out.println(pre);
			}
			return;
		}
		
		int pointIndex = pre.indexOf('.');
		int needMoveStep = pre.length()-1-pointIndex;
		
		int tailZero = subInt -needMoveStep;
		if (tailZero > 0){
			boolean isFirst = true;
			for ( int i = 0; i < pre.length(); i++ ){
				char c = pre.charAt(i);
				if (c == '.'){
					continue;
				}
				if (c == '0' && isFirst){
					continue;
				}
				isFirst = false;
				System.out.print(c);
			}
			for ( int i = 0; i < tailZero; i++ ){
				System.out.print('0');
			}
			
		}else{
			boolean first = true;
			for ( int i = 0; i < pre.length(); i++ ){
				char c = pre.charAt(i);
				if (c == '.'){
					continue;
				}
				if ( c == '0' ){
					if (i < pointIndex + subInt && first
							&& (! ( subInt == 0  && i+1 == pointIndex ) )){
						continue;
					}
				}
				first = false;
				System.out.print(c);
				if ( i == pointIndex + subInt
						 || ( subInt == 0  && i+1 == pointIndex )){
					if ( i != pre.length()-1 ){
						System.out.print('.');
					}
				}
			}
		}
	}
}