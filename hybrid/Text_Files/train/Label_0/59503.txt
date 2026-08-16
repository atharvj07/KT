import java.util.*;
import java.math.*;

class Main{
	public static void main(String[] args){
		Solve s = new Solve();
		s.solve();
	}	
}
class Solve{
	Solve(){}
	
	Scanner in = new Scanner(System.in);

	void solve(){
		while(in.hasNext()){
			String s = in.next();
			if(s.equals(".")) return;
			System.out.println(calc(s, false));
		}
	}

	String calc(String s, boolean isrev){
		StringBuilder ret = new StringBuilder();

		int r = 0;
		char c = 'A';
		for(int i = 0; i < s.length(); i++){
			if(s.charAt(i) == '['){
				int k = i+1, rank = 1;
				while(rank>0){
					//if(k>=s.length()) break;
					if(s.charAt(k)=='[') rank++;
					else if(s.charAt(k)==']') rank--;
					k++;
				}
				//System.out.println("OK");
				ret.append(calc(s.substring(i + 1, k), true));
				i=k-1;
			}
			else if(s.charAt(i)==']') continue;
			else if(s.charAt(i)=='+') r++;
			else if(s.charAt(i)=='-') r--;
			else{
				if(s.charAt(i)=='?') c='A';
				else c = (char)('A'+(s.charAt(i)-'A'+r+26*100)%26);
				r = 0;
				ret.append(c);
			}
		}

		if(isrev) ret.reverse();
		return ret.toString();
	}
	
}

// while(in.hasNext()){
		// 	int n = in.nextInt();
		// 	if(n == 0) return;
			
		// }