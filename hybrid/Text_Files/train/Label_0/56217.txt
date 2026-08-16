import java.util.*;

public class Main{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		int set = sc.nextInt();

		while(set-- > 0){
			int n=sc.nextInt(), m=sc.nextInt();

			int[] t = new int[n];
			int[] s = new int[m];
			for(int i=0;i<n;i++) t[i] = toNum(sc.next());
			for(int i=0;i<m;i++) s[i] = toNum(sc.next());

			System.out.println(solve(t,s,n-1) || solve(t,s,n-2) ?
												 "Yes" : "No");
		}
	}

	private static int toNum(String s){
		if(s.equals("C"))  return 0;
		if(s.equals("C#")) return 1;
		if(s.equals("D"))  return 2;
		if(s.equals("D#")) return 3;
		if(s.equals("E"))  return 4;
		if(s.equals("F"))  return 5;
		if(s.equals("F#")) return 6;
		if(s.equals("G"))  return 7;
		if(s.equals("G#")) return 8;
		if(s.equals("A"))  return 9;
		if(s.equals("A#")) return 10;
		if(s.equals("B"))  return 11;
		return -1;
	}

	private static boolean solve(int[] t,int[] s,int index){
		int i = index;

		for(int j=s.length-1;j>=0;j--){
			if(i < 0 || t.length <= i) return false;
			i += nexts(t[i],s[j]);
		}
		if(i == -1) return true;
		return false;
	}

	private static int nexts(int t,int s){
		if(t == s) return -1;
		if(bound(t-1) == s) return 1;
		if(bound(t+1) == s) return -2;
		return 500000;
	}

	private static int bound(int index){
		return (index + 12) % 12;
	}
}