import java.util.*;

public class Main
{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String s = scanner.nextLine();
		String correct = "hello";
		int loc = 0;
		boolean isSuccess = false;
		Character c = new Character('a');
		Character cor = new Character('a');
		
		for (int i = 0; i < s.length(); i++){
		    c = s.charAt(i);
		    cor = correct.charAt(loc);
		    if (c.equals(cor)){
		        ++loc;
		    }
		    
		    if (loc == 5){
		        isSuccess = true;
		        break;
		    }
		}
		
		if (isSuccess){
		    System.out.println("YES");
		} else {
		    System.out.println("NO");
		}
    }
}
