import java.util.*;
public class Main {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int s=0;
		
		String str=sc.next();
		char[] c=str.toCharArray();
		for(int i=0;i<4;i++){
			if(c[i]=='+'){
				s++;
			}else if(c[i]=='-'){
				s--;
			}
		}
		System.out.println(s);
	}
}