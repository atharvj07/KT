import java.util.*;

public class Main{

    void solve(){
	Scanner sc = new Scanner(System.in);

	int n = sc.nextInt();
	while(n--!=0){

	    String s = sc.next();
	    int winner = 1;
	    for(int i=0; i<s.length()-1; i++){
		String ns = String.valueOf(s.charAt(i)-'0' + s.charAt(i+1)-'0');
		s = ns + s.substring(i+2,s.length());
		i--;
		winner = 1-winner;
	    }

	    System.out.println(winner==1 ? "Audrey wins." : "Fabre wins.");
	}
    }

    public static void main(String[] args){
	new Main().solve();
    }
}