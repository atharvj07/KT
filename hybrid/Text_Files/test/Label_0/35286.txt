import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		char[] ch = scn.nextLine().toCharArray();
		boolean how = (ch[0]==ch[1] && ch[2]==ch[3]&&ch[0]!=ch[2])||(ch[0] == ch[2]&&ch[1]==ch[3]&&ch[0]!=ch[1])||(ch[0]==ch[3]&&ch[1]==ch[2]&&ch[0]!=ch[1]);
		System.out.println(how?"Yes":"No");
	}

}